from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.dispatch import receiver

# Create your models here.

class Neighbourhood(models.Model):
  name = models.CharField(max_length=60)
  logo = CloudinaryField('media')
  admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="hood")
  description = models.TextField(max_length=250)
  location = models.CharField(max_length=60)
  police_number = models.IntegerField()
  health_number = models.IntegerField()

  def __str__(self):
    return f'{self.name} hood'

  def create_neighbourhood(self):
    self.save()

  def delete_neighbourhood(self):
    self.delete()

  @classmethod
  def find_neighbourhood(cls, neighbourhood_id):
    return cls.objects.filter(id=neighbourhood_id)



class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
  name  = models.CharField(max_length=60)
  profile_picture = CloudinaryField('media', null=True)
  bio = models.TextField(max_length=200, null=True, blank=True)
  location = models.CharField(max_length=60, null=True, blank=True)
  email = models.EmailField(max_length=200)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

  def __str__(self):
    return f'{self.user.username} profile'

  def save_profile(self):
    self.user

  def delete_profile(self):
    self.delete()

  @classmethod
  def search_profile(cls, name):
    return cls.objects.filter(user__username__icontains=name).all()



class Business(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  email = models.EmailField(max_length=200)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')

  def __str__(self):
    return f'{self.name} Business'

  def create_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def search_business(cls, name):
    return cls.objects.filter(name__icontains=name).all()



class Post(models.Model):
  title = models.CharField(max_length=100, null=True)
  post = models.TextField(max_length=250)
  date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
  hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, default='', related_name='hood_post')

  def save_post(self):
    self.user

  def delete_post(self):
    self.delete()

  @classmethod
  def search_post(cls, name):
    return cls.objects.filter(title__icontains=title).all()