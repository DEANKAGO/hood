from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.index, name='index'),
  path('all_hoods/', views.all_hoods, name='hood'),
  path('single_hood/<hood_id>', views.single_hood, name='single_hood'),
  path('new_hood/', views.create_hood, name='new_hood'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)