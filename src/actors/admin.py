from django.contrib import admin

# Register your models here.
from .models import Actor

class ActorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio', 'created_at', 'updated_at']
    search_fields = ['name', 'bio']
    list_display_links = ['name']
    list_filter = ['created_at', 'updated_at']
    class Meta:
        model = Actor

admin.site.register(Actor, ActorModelAdmin)