from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ('user', 'neighborhood')



class NeighborhoodForm(forms.ModelForm):
  class Meta:
    model = Neighborhood
    exclude = ('admin')