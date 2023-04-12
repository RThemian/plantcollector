from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plants_detail', kwargs={'plant_id': self.id})

class Pollinator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pollinators_detail', kwargs={'pk': self.id})