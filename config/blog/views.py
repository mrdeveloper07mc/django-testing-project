from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin # userni auth qildi qimadi tekshiradi
# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        # print(self.request.path)
        # print(self.request.get_full_path())
        # print(self.request.get_host())
        # print(self.request.get_port())
        # print(dir(self.request.user))
        # print(self.request.user.is_authenticated)
        return super().get_context_data(**kwargs)