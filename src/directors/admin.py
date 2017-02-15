from django.contrib import admin

# Register your models here.
from .models import Director

class DirectorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio', 'created_at', 'updated_at']
    search_fields = ['name', 'bio']
    list_display_links = ['name']
    list_filter = ['created_at', 'updated_at']
    class Meta:
        model = Director

admin.site.register(Director, DirectorModelAdmin)