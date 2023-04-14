from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Plant, Pollinator, Watering, Photo
from .forms import WateringForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'plantcollector-nov8'


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def plants_index(request):
    return render(request, 'plants/index.html', {'plants': Plant.objects.all()})

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    # create a list of pollinators that belong to the plant
    plant_pollinators_ids = plant.pollinators.all().values_list('id')
    #  flat = True returns a list of ids instead of a list of tuples
    pollinators_plant_doesnt_have = Pollinator.objects.exclude(id__in=plant_pollinators_ids)
    return render(request, 'plants/detail.html', {
        'plant': plant,
        'watering_form': watering_form,
        'pollinators': pollinators_plant_doesnt_have
        })

@login_required
def add_watering(request, plant_id):
    # create a ModelForm instance using the data in request.POST
    # validate user input and save the data to the db
    form = WateringForm(request.POST)
    if form.is_valid():
        # don't save the form to the db until it has the plant_id assigned
        new_watering = form.save(commit=False) # commit=False means don't save to db yet
        new_watering.plant_id = plant_id # assign the plant_id to the watering
        new_watering.save() # save the watering to the db
    return redirect('plants_detail', plant_id=plant_id)

@login_required
def assoc_pollinator(request, plant_id, pollinator_id):
    # find the plant
    plant = Plant.objects.get(id=plant_id)
    # associate the pollinator with the plant
    plant.pollinators.add(pollinator_id)
    return redirect('plants_detail', plant_id=plant_id)

@login_required
def unassoc_pollinator(request, plant_id, pollinator_id):
    # find the plant
    plant = Plant.objects.get(id=plant_id)
    # unassociate the pollinator with the plant
    plant.pollinators.remove(pollinator_id)
    return redirect('plants_detail', plant_id=plant_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        #  create a user using the UserCreationForm
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('plants_index')
        else:
            error_message = 'Invalid sign up - try again'
        
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error_message
        })

def add_photo(request, plant_id):
    # collect photo submitted by user
    photo_file = request.FILES.get('photo-file', None)

    if photo_file:
        # connect to S3
        s3 = boto3.client('s3')

        # create a unique file name
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # upload the file to S3
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, plant_id=plant_id)
        except Exception as error:
            print('An error occurred uploading file to S3', error)
    return redirect('plants_detail', plant_id=plant_id)


       
class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['name', 'description', 'lifespan']
    template_name = 'plants/plant_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model= Plant
    fields = ['name', 'description', 'lifespan']
    template_name = 'plants/plant_form.html'


class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'
    template_name = 'plants/plant_confirm_delete.html'

class PollinatorList(LoginRequiredMixin, ListView):
    model = Pollinator
    template_name = 'pollinators/pollinator_index.html'

class PollinatorDetail(LoginRequiredMixin, DetailView):
    model = Pollinator
    template_name = 'pollinators/pollinator_detail.html'

class PollinatorCreate(LoginRequiredMixin, CreateView):
    model = Pollinator
    fields = '__all__'
    template_name = 'pollinators/pollinator_form.html'

class PollinatorUpdate(LoginRequiredMixin, UpdateView):
    model = Pollinator
    fields = '__all__'
    template_name = 'pollinators/pollinator_form.html'

class PollinatorDelete(LoginRequiredMixin, DeleteView):
    model = Pollinator
    success_url = '/pollinators/'
    template_name = 'pollinators/pollinator_confirm_delete.html'

