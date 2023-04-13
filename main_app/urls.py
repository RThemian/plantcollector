from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


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
        path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
        path('plants/<int:plant_id>/assoc_pollinator/<int:pollinator_id>/', views.assoc_pollinator, name='assoc_pollinator'),
        path('plants/<int:plant_id>/unassoc_pollinator/<int:pollinator_id>/', views.unassoc_pollinator, name='unassoc_pollinator'),
        path('accounts/signup/', views.signup, name='signup'),
        path('plants/<int:plant_id>/add_photo/', views.add_photo, name='add_photo'),
        # redirect to home page after login
        path('accounts/login/', LoginView.as_view(template_name='registration/login.html', next_page='/'), name='login'),
        # redirect to home page after logout
        path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),

    ]