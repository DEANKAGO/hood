from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def index(request):
  return render(request, 'main/index.html')
