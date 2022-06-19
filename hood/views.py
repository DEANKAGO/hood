from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def index(request):
  return render(request, 'main/index.html')


def all_hoods(request):
  all_hoods = Neighborhood.objects.all()
  all_hoods = all_hoods[::-1]
  return render(request, 'main/all_hoods.html', locals())



def single_hood(request, hood_id):
  hood = Neighborhood.objects.get(id=hood_id)
  business = Business.objects.filter(neighborhood=hood)
  posts = Post.objects.filter(hood=hood)
  posts = posts[::-1]
  if request.method == 'POST':
    form = BusinessForm(request.POST)
    if form.is_valid():
      business_form = form.save(commit=False)
      business_form.neighborhood = hood 
      business_form.user = request.user.profile
      business_form.save()
      return render('main/single_hood.html', hood.id)
  else:
    form = BusinessForm()
  context = {
    'hood': hood,
    'business': business,
    'form': form,
    'posts': posts,
  }
  return render(request, 'main/single_hood.html', context)
