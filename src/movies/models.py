from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.

def upload_location(instance, filename):
    return "%s/%s/%s" % (instance.__class__.__name__, instance.id, filename)


class Movie(models.Model):
    name = models.CharField(max_length=120)
    plot = models.TextField()
    release_date = models.DateTimeField()
    rating = models.FloatField(default=0.0)
    photo = models.ImageField(upload_to=upload_location, blank=True, null=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    directors = models.ManyToManyField('directors.Director')
    actors = models.ManyToManyField('actors.Actor')
    user_rating = models.ManyToManyField(User, through='MovieRating')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse("movies:show", kwargs={"id": self.id})


class MovieRating(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    rating = models.FloatField(default=0.0)
