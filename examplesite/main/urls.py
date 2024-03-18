from django.urls import path
from django.http import HttpResponse
from . import views

app_name = "main"

urlpatterns = [
    path('',views.HomePageView.as_view(),name="home" ),
    path('leguage/<pk>', views.LeaguageDetailView.as_view(), name='leaguage_detail'),
    
    path("club/<pk>", views.ClubDetailView.as_view(), name='club_detail'),
    path("player/<pk>", views.PlayerDetailView.as_view(), name='player_detail')
]


# views - asosiy logika 
# controller method  - def 
# controller class - class 