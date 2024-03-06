from django.urls import path
from django.http import HttpResponse
from . import views

app_name = "main"

urlpatterns = [
    path('',views.HomePageView.as_view(),name="home" )
]


# views - asosiy logika 
# controller method  - def 
# controller class - class 