from django.urls import path
from django.contrib.auth.views import * # standart login sahifasi views

from .import views


app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="auth/login.html"), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    
    path("register/",views.register, name='register'),
    path("password_change/",PasswordChangeView.as_view(
        template_name="auth/password_change_form.html",
        success_url="/"
        ), name='password_change'),
    
    path("password-reset/", PasswordResetView.as_view(
        template_name="auth/password_reset_form.html",), name='password_reset'),
    path("password-reset-done/", PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("password-reset-confirm/", PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("password-reset-complete/", PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
