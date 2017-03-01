"""imdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from .views import (
    movies_index,
    movie_show,
    movie_rating,
    create_movie_review,
    edit_movie_review,
    delete_movie_review
)

urlpatterns = [
    url(r'^$', movies_index),
    url(r'^(?P<id>\d+)/$', movie_show, name='show'),
    url(r'^(?P<id>\d+)/rating/$', movie_rating, name='rating'),
    url(r'^(?P<id>\d+)/review/$', create_movie_review, name='new_review'),
    url(r'^(?P<movie_id>\d+)/reviews/(?P<id>\d+)$', edit_movie_review, name='edit_review'),
    url(r'^(?P<movie_id>\d+)/reviews/(?P<id>\d+)/delete$', delete_movie_review, name='delete_review'),
]
