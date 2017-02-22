from django.shortcuts import render
from directors.models import Director
from actors.models import Actor
from movies.models import Movie

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
