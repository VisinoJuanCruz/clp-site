from django.shortcuts import render
from .models import Player, Country, Rank, Person, Agent, Map,Rol
from django.views import generic
def index(request):
    """ Funcion vista para la pagina de inicio del sitio"""
    num_players = Player.objects.all().count()
    num_maps = Map.objects.all().count() 
    num_agents = Agent.objects.all().count()

    return render(
            request,
            'index.html',
            context={'num_players':num_players,
            'num_maps':num_maps,
            'num_agents':num_agents})
   
class PlayerListView(generic.ListView):
    model = Player

class PlayerDetailView(generic.DetailView):
    model = Player

class MapListView(generic.ListView):
    model = Map

class MapDetailView(generic.DetailView):
    model = Map

class AgentListView(generic.ListView):
    model = Agent

class AgentDetailView(generic.DetailView):
    model = Agent
