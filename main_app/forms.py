from django.forms import ModelForm
from .models import Feature

class FeatureForm(ModelForm):
  class Meta:
    model = Feature
    fields = ['date', 'value']