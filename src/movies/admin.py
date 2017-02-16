from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'plot', 'created_at', 'updated_at']
    search_fields = ['name', 'plot']
    list_display_links = ['name']
    list_filter = ['created_at', 'updated_at']
    class Meta:
        model = Movie

admin.site.register(Movie, MovieModelAdmin)