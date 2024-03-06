from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

# TemplateView - oddiy htmlni response sifatida qaytarish
class HomePageView(TemplateView):
    template_name = "index.html"