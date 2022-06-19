from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ('user', 'neighbourhood')



class NeighbourhoodForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    exclude = ('admin')


class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ('user', 'neighbourhood')


