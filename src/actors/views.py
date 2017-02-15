from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Actor
# Create your views here.

def actors_index(request):
    actors = Actor.objects.all()
    context_data = {
        'directors': actors
    }
    return render(request, 'actors/index.html', context_data)

def actors_show(request, id=None):
    actor = get_object_or_404(Actor, id=id)
    context_data = {
        'director': actor,
        'title': actor.name
    }
    return render(request, 'actors/show.html', context_data)
