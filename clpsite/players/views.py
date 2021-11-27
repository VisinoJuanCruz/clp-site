from django.shortcuts import render
from .models import Player, Country, Rank, Person, Agent, Map,Rol
from django.views import generic
def index(request):
    """ Funcion vista para la pagina de inicio del sitio"""
    num_players = Player.objects.all().count()
    


    return render(
            request,
            'index.html',
            context={'num_players':num_players},)
   
class PlayerListView(generic.ListView):
    model = Player

class PlayerDetailView(generic.DetailView):
    model = Player
