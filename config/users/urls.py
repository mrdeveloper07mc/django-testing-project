from django.urls import path
from django.contrib.auth.views import LoginView # standart login sahifasi views

from .import views


app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="auth/login.html"), name='login')
    
]
