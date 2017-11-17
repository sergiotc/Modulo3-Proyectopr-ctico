"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import Videogames
from app.forms import Gameform

def home(request):
    games = Videogames.objects.all().order_by('name')
    return render(
        request,
        'app/index.html',
        {
            "games" : games,
        }
    )

def paginagame(request, id):
    game = Videogames.objects.get(pk=id)
    return render(request,
                 'app/PaginaGame.html',
                 { "game" : game }
                 )

def crear_game(request):
    if request.method == 'POST':
        
        # Formulario rellenado, guardarlo
        formulario = Gameform(request.POST)
        if formulario.is_valid():
            #guardamos el formulario
            game = formulario.save()
            return HttpResponseRedirect('/game/' + str(game.id))

    elif request.method == 'GET':
        # Peticion de formulario, mandar uno
        formulario = Gameform()
        return render(request,
                    'app/Gameform.html',
                    { 'form' : formulario,
                      'action': "/crear"}
                    )
    else:
        return render(request, )

def modificar_game(request, id):

    game = Videogames.objects.get(pk=id)
    if request.method == 'POST':
        formulario = Gameform(request.POST, instance=game)
        if formulario.is_valid():
            game = formulario.save()
            return HttpResponseRedirect("/game/" + str(game.id))

    elif request.method == 'GET':
        formulario = Gameform(instance = game)
        return render(request,
                      'app/Gameform.html',
                      {'form': formulario,
                       'action' : '/modificar/' + str(game.id)}
                      )
    else:
        return render(request)
def borrar_game(request, id):
    game = Videogames.objects.get(pk=id)
    game.delete()
    return HttpResponseRedirect('/')

def ranking(request):
        rankings = Videogames.objects.all().order_by('score')
        return render(
            request,
            'app/Ranking.html',
            {
                "rankings" : rankings,
            }
        )