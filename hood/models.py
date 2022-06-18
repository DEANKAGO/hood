from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.

class Neighborhood(models.Model):
  name = models.CharField(max_length=60)
  logo = CloudinaryField('media', null=True)
  # admin = models.ForeignKey("Profile", on_delete.CASCADE, related_name="hood")
  description = models.TextField()
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
  name  = models.CharField(max_length=60, null=True, blank=True)
  

