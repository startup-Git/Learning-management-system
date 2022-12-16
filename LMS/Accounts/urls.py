from django.urls import path

from .forms import LoginForm
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='Login_Authentication/login.html', authentication_form=LoginForm), name='login'),
    path('registration/', views.RegistrationView.as_view(), name="registration"),

]