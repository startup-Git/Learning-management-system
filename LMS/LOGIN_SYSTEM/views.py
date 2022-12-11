from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .forms import RegistationForm
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'login.html', locals())

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistationForm()
        return render(request, 'registration.html', locals())
    def post(self, request, *args, **kwargs):
        form = RegistationForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulation! User Register Successfully. You can log in now!')
            return redirect('/registration/login/')
        else:
            messages.error(request, 'Please! insert valid data.')
            form = RegistationForm()
        return render(request, 'registration.html', locals())

