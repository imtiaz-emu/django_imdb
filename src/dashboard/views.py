from django.shortcuts import render
from directors.models import Director
from actors.models import Actor
from movies.models import Movie
from django.db.models import Q

# Create your views here.
def index(request):
    directors = Director.objects.all()
    movies = Movie.objects.all().prefetch_related('directors', 'actors')
    actors = Actor.objects.all()
    total_counts = {'movies': len(movies), 'directors': len(directors), 'actors': len(actors)}
    context_data = {
        'directors': directors.order_by('-id')[:2],
        'actors': actors.order_by('-id')[:2],
        'movies': movies.order_by('-id')[:2],
        'counts': total_counts
    }
    return render(request, 'dashboard/index.html', context_data)

def search(request):
    param = request.GET.get('q')
    query_movies = Q(name__icontains = param) | Q(plot__icontains = param)
    query_others = Q(name__icontains = param) | Q(bio__icontains = param)
    movies = Movie.objects.filter(query_movies)
    directors = Director.objects.filter(query_others)
    actors = Actor.objects.filter(query_others)
    total_counts = {'movies': len(movies), 'directors': len(directors), 'actors': len(actors)}
    # print total_counts
    context_data = {
        'directors': directors.order_by('-id'),
        'actors': actors.order_by('-id'),
        'movies': movies.order_by('-id'),
        'counts': total_counts
    }
    return render(request, 'dashboard/search_results.html', context_data)