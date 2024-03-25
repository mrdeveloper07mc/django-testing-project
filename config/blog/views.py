from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin # userni auth qildi qimadi tekshiradi
# Create your views here.


class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = "index.html"