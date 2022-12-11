from django.urls import path

from LOGIN_SYSTEM.forms import LoginForm
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.RegistrationView.as_view(), name="registration"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),


    
]