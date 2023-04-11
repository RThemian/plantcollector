from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Plant
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
    