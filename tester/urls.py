from django.urls import path 
from .import views


app_name = 'tester'

urlpatterns = [
	path('', views.index , name='index')
]