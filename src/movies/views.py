from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Movie, MovieRating, Review
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django.http import HttpResponseRedirect

# Create your views here.

def movies_index(request):
    movies = Movie.objects.all().prefetch_related('directors', 'actors')

    context_data = {
        'movies': movies
    }

    return render(request, 'movies/index.html', context_data)


def movie_show(request, id=None):
    movie = get_object_or_404(Movie.objects.prefetch_related('directors', 'actors', 'review_set'), id=id)
    context_data = {
        'movie': movie,
        'title': movie.name,
        'rating': get_movie_rating(request, movie)
    }
    return render(request, 'movies/show.html', context_data)


def movie_rating(request, id=None):
    movie = get_object_or_404(Movie.objects, id=id)
    if request.is_ajax():
        ratings_given = float(request.GET['rating'])
        try:
            movie_rating = MovieRating.objects.get(user=request.user, movie=movie)
            movie_rating.rating = ratings_given
            movie_rating.save()
            update_movie_rating(movie)
        except ObjectDoesNotExist:
            MovieRating.objects.create(user_id=request.user.id, movie_id=movie.id, rating=ratings_given)
            update_movie_rating(movie)

        return JsonResponse({'rating': ratings_given})
    return JsonResponse({'rating': movie.rating})


def create_movie_review(request, id=None):
    movie = get_object_or_404(Movie.objects, id=id)
    has_spoiler = 0 if 'has_spoiler' not in request.POST else request.POST['has_spoiler']
    Review.objects.create(user_id=request.user.id, movie_id=movie.id,
                          title=request.POST['title'], description=request.POST['description'],
                          has_spoiler=has_spoiler)
    return HttpResponseRedirect(movie.get_absolute_url())


def edit_movie_review(request, movie_id=None, id=None):
    movie = get_object_or_404(Movie.objects, id=movie_id)
    review = get_object_or_404(Review.objects, id=id)
    review.title = request.POST['title']
    review.description = request.POST['description']
    review.has_spoiler = 0 if 'has_spoiler' not in request.POST else request.POST['has_spoiler']
    review.save(update_fields=['title', 'description', 'has_spoiler'])

    return HttpResponseRedirect(movie.get_absolute_url())

def delete_movie_review(request, movie_id=None, id=None):
    movie = get_object_or_404(Movie.objects, id=movie_id)
    review = get_object_or_404(Review.objects, id=id)
    review.delete()
    return HttpResponseRedirect(movie.get_absolute_url())

def update_movie_rating(movie):
    result = MovieRating.objects.filter(movie_id=movie.id).aggregate(Avg('rating'))
    movie.rating = result['rating__avg']
    movie.save(update_fields=['rating'])

def get_movie_rating(request, movie):
    if request.user.is_authenticated():
        rating = MovieRating.objects.filter(user=request.user, movie=movie)
        if len(rating) > 0:
            return rating[0].rating

    return movie.rating
