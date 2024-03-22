from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView ,DetailView
from .models import Club,Leaguage,Player
# Create your views here.

# TemplateView - oddiy htmlni response sifatida qaytarish
# ListView - korsatilgan modeldan ma'lumotlarn olib korsatilgan html ga "object_list" keyida jonatadi

class HomePageView(ListView):
    model = Leaguage
    # context_object_name = "ligalar"
    template_name = "index.html"
    
    # htmlga jonatiladigan ma'lumotlarni boshqarish metodi 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        context["players"] = Player.objects.all() # barcha objectlarni olish
        
        # first_player = Player.objects.get(id=1) # faqat 1 ta object
        # print(first_player)
        # first_player = Player.objects.get(id=1) # faqat 1 ta object
        # print(first_player)
        # get_or_cretae_player = Player.objects.get_or_create() # 1 ta object olish yoki hosil qilish
        # __exact - aniq yozilgan matn boyicha filter
        # __iexact - aniq yozilgan matn boyicha filter katta yoki kichkina harf farqi yoq
        # __contains - berilgan matn maydonda mavjud yoki yoqligiga tekshirish
        # __icontains - berilgan matn maydonda mavjud yoki yoqligiga tekshirish katta yoki kichkina harf farqi yoq
        # __gt - katta
        # __gte - katta yoki teng 
        # __lt - kichik 
        # __lte - kichik yoki teng
        # __stratswith - berilgan matn bilan boshlansa 
        # __istratswith - berilgan matn bilan boshlansa katta yoki kichkina harf farqi yoq
        # __endswith - berilgan matn bilan tugasa 
        # __iendswith - berilgan matn bilan tugasa katta yoki kichkina harf farqi yoq
        # __range - ma'lum bir diapazondagilarni filterlash
        # filtering_players = Player.objects.filter(height__range=(150,180))
        # for p in filtering_players:
        #     print(p.name)
        #     print(p.height)
        # import datetime
        # date = datetime.date.today()
        # this_week = date - datetime.timedelta(date.weekday())
        # players_of_this_week = Player.objects.filter(created_at__in=this_week)
        # print(players_of_this_week)
        # __in - berilgan qiymatlarga mos objectlarni filterlash
        # players_of_same_country = Player.objects.filter(country__in=["Angliya","Braziliya"])
        # print(players_of_same_country)
        
        # players_all_not_english = Player.objects.all().exclude(country="Angliya")
        # print(players_all_not_english)
        altay = Player.objects.get(name="Altay Bayındır")
        # update 
        # altay.name = "Altay Bayındırjon"
        # altay.save()
        # delete 
        # altay.delete() 
        # new_club = Club.objects.create(name="Atletik" .... )
        
        # CRUD - Create , Retrive, Update , Delete 
        return context
    

class LeaguageDetailView(DetailView):
    model = Leaguage
    template_name = "leaguage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object - DetailView orqal modeldan olinayotgan obyekt
        context["clubs"] = Club.objects.filter(leaguage=self.object)

        return context
  
class ClubDetailView(DetailView):
    model = Club
    template_name = "club.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object - DetailView orqal modeldan olinayotgan obyekt
        context["players"] = Player.objects.filter(club=self.object)

        return context


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player.html'
    
    



class CantactPageView(TemplateView):
    template_name = "contact.html"
    
    

def filter_by_position(request):
    if request.method  == "POST":
        pos = request.POST.get("position")
        players = Player.objects.filter(position=pos)
        data = {
            "players":players
        }
    return render(request, 'result.html', context=data)


def filter_by_age(request):
    if request.method  == "POST":
        min_age_range = request.POST.get("min_age")
        max_age_range = request.POST.get("max_age")
        players = Player.objects.filter(date_of_birth__range=[min_age_range,max_age_range])
        data = {
            "players":players
        }
    return render(request, 'result.html', context=data)