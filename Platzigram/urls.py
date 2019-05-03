"""Platzigram URL Configuration"""
from django.contrib import admin
from django.urls import path
from Platzigram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello-world', local_views.hello_world),
    path('posts/', posts_views.list_posts),
    path('stored/', local_views.sort_integers),

    path('hi/<str:name>/<int:age>', local_views.say_hi),
]
