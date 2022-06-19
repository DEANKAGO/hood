from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def index(request):
  return render(request, 'main/index.html')


def profile(request, username):
  return render(request, 'main/profile.html')


def update_profile(request, username):
  user = user.objects.get(username=username)
  if request.method == 'POST':
    form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if form.is_valid():
      form.save()
      return redirect('profile', user.username)
  else:
    form = UpdateProfileForm(instance=request.user.profile)
  return render(request, 'main/update_profile.html', {'form': form})




def all_hoods(request):
  all_hoods = Neighbourhood.objects.all()
  all_hoods = all_hoods[::-1]
  return render(request, 'main/all_hoods.html', locals())



def single_hood(request, hood_id):
  hood = Neighbourhood.objects.get(id=hood_id)
  business = Business.objects.filter(neighbourhood=hood)
  posts = Post.objects.filter(hood=hood)
  posts = posts[::-1]
  if request.method == 'POST':
    form = BusinessForm(request.POST)
    if form.is_valid():
      business_form = form.save(commit=False)
      business_form.neighbourhood = hood 
      business_form.user = request.user.profile
      business_form.save()
      return render('single_hood', hood.id)
  else:
    form = BusinessForm()
  context = {
    'hood': hood,
    'business': business,
    'form': form,
    'posts': posts,
  }
  return render(request, 'main/single_hood.html', context)



def create_hood(request):
  if request.method == 'POST':
    form = NeighbourhoodForm(request.POST, request.FILES)
    if form.is_valid():
      hood = form.save(commit=False)
      hood.admin = request.user.profile
      hood.save()
      return redirect('hood')
  else:
    form = NeighbourhoodForm()
  return render(request, 'main/create_hood.html',)



def members(request, hood_id):
  hood = Neighbourhood.objects.get(id=hood_id)
  members = Profile.objects.filter(neighbourhood=hood)
  return render(request, 'main/members.html', {'members': members})



def join_hood(request, id):
  neighbourhood = get_object_or_404(Neighbourhood, id=id)
  request.user.profile.neighbourhood = neighbourhood
  request.user.profile.save()
  return redirect('hood')


def leave_hood(request, id):
  hood = get_object_or_404(Neighbourhood, id=id)
  request.user.profile.neighbourhood = None
  request.user.profile.save()
  return redirect('hood')


def search_business(request):
  if request.method == 'GET':
    name = request.GET.get('title')
    results = Business.objects.filter(name__icontains=name).all()
    message = f'name'
    context = {
      'results': results,
      'message': message
    }
    return render(request, 'main/results.html', context)
  else:
    message = 'Search a category for results'
  return render(request, 'main/results.html')


def create_post(request, hood_id):
  hood = Neighbourhood.objects.get(id=hood_id)
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save()
      post.hood = hood
      post.user = request.user.profile
      post.save()
      return redirect('single_hood', hood.id)
  else:
    form = PostForm()
  return render(request, 'main/post.html', {'form': form})