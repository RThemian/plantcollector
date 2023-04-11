from django.urls import path
from . import views

urlpatterns = [  
        path('', views.home),  
        path('about/', views.about, name="about"), # path('about/', views.about, name ="about"),
        path('plants/', views.plants_index, name='plants_index'),
        path('plants/<int:plant_id>/', views.plants_detail, name='plants_detail'),
        path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
        
    ]