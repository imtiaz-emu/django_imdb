from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Director
# Create your views here.

def director_index(request):
    directors = Director.objects.all()
    context_data = {
        'directors': directors
    }
    return render(request, 'directors/index.html', context_data)

def director_show(request, id=None):
    director = get_object_or_404(Director, id=id)
    context_data = {
        'director': director,
        'title': director.name
    }
    return render(request, 'directors/show.html', context_data)

def director_create(request):
    return HttpResponse("<h1>Director Create</h1>")

def director_update(request):
    return HttpResponse("<h1>Director Update</h1>")

def director_delete(request):
    return HttpResponse("<h1>Director Delete</h1>")
