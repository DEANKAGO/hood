from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.index, name='index'),
  path('profile/<username>', views.profile, name='profile'),
  path('all_hoods/', views.all_hoods, name='hood'),
  path('single_hood/<hood_id>', views.single_hood, name='single_hood'),
  path('new_hood/', views.create_hood, name='new_hood'),
  path('<hood_id>/members', views.members, name='members'),
  path('join_hood/<id>', views.join_hood, name='join_hood'),
  path('leave_hood/<id>', views.leave_hood, name='leave_hood'),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)