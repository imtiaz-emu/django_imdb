from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'plot', 'director', 'release_date']
    search_fields = ['name', 'plot']
    list_display_links = ['name']
    list_filter = ['created_at', 'updated_at']
    class Meta:
        model = Movie

    def director(self, instance):
        return instance.directors.values_list('name', flat=True)

admin.site.register(Movie, MovieModelAdmin)