from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Actor
# Create your views here.

def actors_index(request):
    actors = Actor.objects.all()
    context_data = {
        'actors': actors
    }
    return render(request, 'actors/index.html', context_data)

def actors_show(request, id=None):
    actor = get_object_or_404(Actor.objects.prefetch_related('movie_set'), id=id)
    context_data = {
        'actor': actor,
        'title': actor.name
    }
    return render(request, 'actors/show.html', context_data)
