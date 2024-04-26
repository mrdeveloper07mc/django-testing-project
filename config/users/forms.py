
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username","first_name","email","password1","password2"]

        
import telebot

bot.send_message('-22222' ,message)