from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse("actors:show", kwargs={"id": self.id})