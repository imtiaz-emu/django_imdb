from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def movies_index(request):
    movies = Movie.objects.all().prefetch_related('directors', 'actors')

    context_data = {
        'movies': movies
    }

    return render(request, 'movies/index.html', context_data)

def movie_show(request, id=None):
    movie = get_object_or_404(Movie.objects.prefetch_related('directors', 'actors'), id=id)
    context_data = {
        'movie': movie,
        'title': movie.name
    }
    return render(request, 'movies/show.html', context_data)
