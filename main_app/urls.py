from django.urls import path
from . import views

urlpatterns = [  
        path('', views.home),  
        path('about/', views.about, name="about"), # path('about/', views.about, name ="about"),
        path('plants/', views.plants_index, name='plants_index'),
        path('plants/<int:plant_id>/', views.plants_detail, name='plants_detail'),
        path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
        path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
        path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
        path('pollinators/', views.PollinatorList.as_view(), name='pollinators_index'),
        path('pollinators/<int:pk>/', views.PollinatorDetail.as_view(), name='pollinators_detail'),
        path('pollinators/create/', views.PollinatorCreate.as_view(), name='pollinators_create'),
        path('pollinators/<int:pk>/update/', views.PollinatorUpdate.as_view(), name='pollinators_update'),
        path('pollinators/<int:pk>/delete/', views.PollinatorDelete.as_view(), name='pollinators_delete'),
    ]