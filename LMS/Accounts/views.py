from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .forms import RegistationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def login(request):
    return render(request, 'Login_Authentication/login.html', locals())

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistationForm()
        return render(request, 'Login_Authentication/registration.html', locals())
    def post(self, request, *args, **kwargs):
        form = RegistationForm(request.POST)
        if form:
            email = request.POST.get('email')
            username = request.POST.get('username')
            # check email
            if User.objects.filter(email = email).exists():
                messages.warning(request, 'Email are already exists.')
                return redirect('registration/')
            # check usename
            if User.objects.filter(username = username).exists():
                messages.warning(request, 'username are already exists.')
                return redirect('registration/')
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulation! User Register Successfully. You can log in now!')
            return redirect('/accounts/login/')
        else:
            form = RegistationForm()
        return render(request, 'Login_Authentication/registration.html', locals())


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Profile/profile.html', locals())

    def post(self, request, *args, **kwargs):
        return render(request, 'Profile/profile.html', locals())

def profileUpdate(request):
    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        username = request.POST.get('UserName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request, 'Your Profile are successfully updated.')
    return redirect('/accounts/profile/')