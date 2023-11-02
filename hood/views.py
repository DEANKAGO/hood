from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        procForm = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            # username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()
        return redirect('login')
    else:
        form = RegistrationForm()
        profForm = ProfileForm()
    params={
        'form':form,
        'profForm': profForm,
    }
    return render(request, 'registration/register.html', params)



def index(request):
  return render(request, 'main/index.html')


def profile(request, username):
  return render(request, 'main/profile.html')


def update_profile(request):
  user = request.user
  # user = user.objects.get(username=username)
  if request.method == 'POST':
    user_form = UserUpdateForm(request.POST, instance=request.user)
    prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if user_form.is_valid() and prof_form.is_valid():
      user_form.save()
      prof_form.save()
      return redirect('profile', user.id)
  else:
    user_form = UserUpdateForm(instance=request.user)
    prof_form = UpdateProfileForm(instance=request.user.profile)
  context = {
    'user_form': user_form,
    'prof_form': prof_form
  }
  return render(request, 'main/update_profile.html', context )




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
      return redirect('single_hood', hood_id)
  else:
    form = BusinessForm()
  context = {
    'hood': hood,
    'business': business,
    'form': form,
    'posts': posts,
  }
  return render(request, 'main/single_hood.html', context)


@login_required(login_url='login') 
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
  return render(request, 'main/create_hood.html', {'form': form})



def members(request, hood_id):
  hood = Neighbourhood.objects.get(id=hood_id)
  members = Profile.objects.filter(neighbourhood=hood)
  return render(request, 'main/members.html', {'members': members})


@login_required(login_url='login') 
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
    message = 'Search a business name for results'
  return render(request, 'main/results.html')

@login_required(login_url='login') 
def create_post(request, hood_id):
  # hood = Neighbourhood.objects.get(id=hood_id)
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      # post.hood = hood
      post.user = request.user.profile
      post.save()
      return redirect('single_hood', hood_id)
  else:
    form = PostForm()
  return render(request, 'main/post.html', locals())