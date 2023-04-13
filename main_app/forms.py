from django.forms import ModelForm 
from .models import Watering

# create a feeding form

class WateringForm(ModelForm):
    # Meta class is a nested class that tells Django which model to base the form off of
    # and which fields to include in the form, and any special options we want to include
    # Meta class is useful because it allows us to keep our form code separate from our model code
    class Meta:
        model = Watering
        fields = ('date', 'hydration')

