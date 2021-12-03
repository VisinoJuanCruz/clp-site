from django.shortcuts import render
from .models import Player, Country, Rank, Person, Agent, Map,Rol
from django.views import generic
from django.http import HttpResponseRedirect

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


def upload_image(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html')
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Image(  image = form.cleaned_data["image"],
                                name = form.cleaned_data["name"]
                                )
            new_image.save()
            return HttpResponseRedirect('/players/upload_image/')
