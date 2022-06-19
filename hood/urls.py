from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('register/', views.register, name='signup'),
  path('account/', include('django.contrib.auth.urls')),
  path('', views.index, name='index'),
  path('profile/<username>', views.profile, name='profile'),
  path('profile/<username>/edit/', views.update_profile, name='update_profile'),
  path('all_hoods/', views.all_hoods, name='hood'),
  path('single_hood/<hood_id>', views.single_hood, name='single_hood'),
  path('new_hood/', views.create_hood, name='new_hood'),
  path('<hood_id>/members', views.members, name='members'),
  path('join_hood/<id>', views.join_hood, name='join_hood'),
  path('leave_hood/<id>', views.leave_hood, name='leave_hood'),
  path('search/', views.search_business, name='search'),
  path('<hood_id>/new_post', views.create_post, name='post'),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)