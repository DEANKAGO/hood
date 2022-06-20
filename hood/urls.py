from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('register/', views.register, name='signup'),
  path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
  path('', views.index, name='index'),
  path('profile/<username>', views.profile, name='profile'),
  path('update_profile/', views.update_profile, name='update_profile'),
  path('all_hoods/', views.all_hoods, name='hood'),
  path('single_hood/<hood_id>', views.single_hood, name='single_hood'),
  path('new_hood/', views.create_hood, name='new_hood'),
  path('members/<hood_id>', views.members, name='members'),
  path('join_hood/<id>', views.join_hood, name='join_hood'),
  path('leave_hood/<id>', views.leave_hood, name='leave_hood'),
  path('search/', views.search_business, name='search'),
  path('new_post/<hood_id>', views.create_post, name='post'),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)