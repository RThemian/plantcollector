from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Plant, Pollinator
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants': Plant.objects.all()})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})

class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'description', 'lifespan']
    template_name = 'plants/plant_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(UpdateView):
    model= Plant
    fields = ['name', 'description', 'lifespan']
    template_name = 'plants/plant_form.html'


class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'
    template_name = 'plants/plant_confirm_delete.html'

class PollinatorList(ListView):
    model = Pollinator
    template_name = 'pollinators/index.html'

class PollinatorDetail(DetailView):
    model = Pollinator
    template_name = 'pollinators/detail.html'

class PollinatorCreate(CreateView):
    model = Pollinator
    fields = '__all__'
    template_name = 'pollinators/pollinator_form.html'

class PollinatorUpdate(UpdateView):
    model = Pollinator
    fields = '__all__'
    template_name = 'pollinators/pollinator_form.html'

class PollinatorDelete(DeleteView):
    model = Pollinator
    success_url = '/pollinators/'
    template_name = 'pollinators/pollinator_confirm_delete.html'
