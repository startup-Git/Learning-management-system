from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .forms import RegistationForm
from django.contrib import messages
from django.contrib.auth.models import User

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
