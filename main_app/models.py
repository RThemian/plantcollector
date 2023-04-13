from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.
class Pollinator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pollinators_detail', kwargs={'pk': self.id})


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pollinators = models.ManyToManyField(Pollinator)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plants_detail', kwargs={'plant_id': self.id})


    
class Watering(models.Model):
    HYDRATIONS = (
        ('M', 'Morning'),
        ('N', 'Noon'),
        ('E', 'Evening'),
    )

    date = models.DateField('Watering Date')
    hydration = models.CharField(
        max_length=1,
        choices=HYDRATIONS,
        default=HYDRATIONS[0][0]
    )

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_hydration_display()} on {self.date}"

    class Meta:
        ordering = ('-date',)

class Photo(models.Model):
   url = models.CharField(max_length=200)
   plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

   def __str__(self):
      return f"Photo for plant_id: {self.plant.id} @{self.url}"