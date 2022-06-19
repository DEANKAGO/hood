from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.dispatch import receiver

# Create your models here.

class Neighborhood(models.Model):
  name = models.CharField(max_length=60)
  logo = CloudinaryField('media', null=True)
  admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="hood")
  description = models.TextField(max_length=250, null=True, blank=True)
  location = models.CharField(max_length=60)
  police_number = models.IntegerField(null=True, blank=True)
  health_number = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return f'{self.name} hood'

  def create_neighborhood(self):
    self.save()

  def delete_neighborhood(self):
    self.delete()

  @classmethod
  def find_neighborhood(cls, neighborhood_id):
    return cls.objects.filter(id=neighborhood_id)



class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
  name  = models.CharField(max_length=60)
  profile_picture = CloudinaryField('media', null=True)
  bio = models.TextField(max_length=200, null=True, blank=True)
  location = models.CharField(max_length=60, null=True, blank=True)
  email = models.EmailField(max_length=200)
  neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

  def __str__(self):
    return f'{self.user.username} profile'

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Business(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  email = models.EmailField(max_length=200)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
  neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='business')

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
  post = models.TextField(max_length=250, null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)



