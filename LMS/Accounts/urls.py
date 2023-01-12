from django.urls import path
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from . import views
from django.contrib.auth import views as auth_view
from django.contrib.auth import authenticate, login


urlpatterns = [
    # Login_Authentication
    path('login/', auth_view.LoginView.as_view(template_name='Login_Authentication/login.html', authentication_form=LoginForm), name='login'),
    path('registration/', views.RegistrationView.as_view(), name="registration"),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='Login_Authentication/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/password-change-done'), name='password-change'),
    path('password-change-done/', auth_view.PasswordChangeDoneView.as_view(template_name='Login_Authentication/passwordchangedone.html'), name='password-change-done'),
    # update_password
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='update_password/password_reset.html', form_class=MyPasswordResetForm), name='password-reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='update_password/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='update_password/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='update_password/password_reset_complete.html'), name='password_reset_complete'),
    # Profile
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path("profile/update", views.profileUpdate, name="profileUpdate")



]