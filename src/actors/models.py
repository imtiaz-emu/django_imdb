from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s/%s" % (instance.__class__.__name__, instance.id, filename)

class Actor(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField()
    photo = models.ImageField(upload_to=upload_location, blank=True, null=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse("actors:show", kwargs={"id": self.id})