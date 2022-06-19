from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
  email = forms.EmailField(max_length=200, help_text='Required, Input a valid email address.')

  class Meta:
    model = User
    fields = ('username','email', 'password1', 'password2')


class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ('user', 'neighbourhood')



class NeighbourhoodForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    exclude = ('admin',)


class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ('user', 'hood')