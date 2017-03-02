from rest_framework.serializers import ModelSerializer
from directors.models import Director
from movies.models import Movie

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'name'
        ]

class DirectorSerializer(ModelSerializer):
    movie_set = MovieSerializer(many=True)
    class Meta:
        model = Director
        fields = [
            'id',
            'name',
            'movie_set'
        ]