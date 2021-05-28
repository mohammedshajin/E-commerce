from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from .import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout') ,
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile', views.profile, name='profile')
]