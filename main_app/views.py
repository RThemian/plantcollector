from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html')

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    template_name = 'plants/plant_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    