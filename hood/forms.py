from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field 
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions
from django.forms import ModelForm


# class SignupForm(UserCreationForm):
#   email = forms.EmailField(max_length=200, help_text='Required, Input a valid email address.')

#   class Meta:
#     model = User
#     fields = ['username','email', 'password1', 'password2']

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:        
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profile_picture','bio']



class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ['name','description','email']



class NeighbourhoodForm(ModelForm):
  helper = FormHelper()

  class Meta:
    model = Neighbourhood
    fields = ['name','description','logo', 'location', 'police_number', 'health_number']


class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email'] 


class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['bio','profile_picture']


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','post', 'hood']