from rest_framework.generics import ListAPIView
from directors.models import Director
from .serializers import DirectorSerializer

class DirectorListApiView(ListAPIView):
    queryset = Director.objects.all().prefetch_related('movie_set')
    serializer_class = DirectorSerializer