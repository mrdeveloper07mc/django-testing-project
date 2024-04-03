from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserRegisterForm
from .models import Profile
# Create your views here.


def register(request):
    form = CustomUserRegisterForm()
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) # yangi profil ochish va uni userga biriktirish
            login(request,user) # auth usermi login qilish
            return redirect("/")
        else:
            print("Error")
            return render(request, "auth/register.html")
    return render(request, "auth/register.html", context={"form":form})

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'auth/profile.html'

# UpdateView - korsatilgan model objectnini bittasini alohida sahifada update qilish imkonini beradi 
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "auth/profile_form.html"
    # fields = "__all__"  # modelni hamma maydoni forma bolib chiqadi
    fields = ["image","bio","date_of_birth", "gender", "country"] 
    # yoki shu tarzda istalgan maydonlarnigina forma qilish mumkin
    
    # hamma ishlar bajarilib muvafaqiyatli ortga qaytish uchun manzilni hosil qilivchi method 
    def get_success_url(self):
        return reverse("users:profile", kwargs={"pk":self.object.id})