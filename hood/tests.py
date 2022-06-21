from django.test import TestCase
from .models import *

# Create your tests here.

class Neighbourhood(TestCase):
  def setup(self):
    self.hood = Neighbourhood(name='Neighbourhood', description='my hood', logo='jirani.jpg', police_number=123, health_number=1337)

  def test_instance(self):
    self.assertTrue(isinstance(self.hood, Neighbourhood))

  def test_Create_Neighbourhood(self):
    self.assertTrue(isinstance(self.hood, Neighbourhood))

  def test_delete_Neighbourhood(self):
    neighbourhood.objects.all().delete()


class BusinessTestCase(TestCase):

  def setup(self):
    self.business = Business(name='Business', description='mY business', email='asd@asd.com')

  def test_instance(self):
    self.assertTrue(isinstance(self.business, Business))

  def test_save_business(self):
    self.business.save_business()
    business = Business.objects.all()
    self.assertTrue(len(business)>0)

  def test_create_business(self):
    self.assertTrue(isinstance(self.business, Business))


  def test_delete_business(self):
    Business.objects.all().delete()