# bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example URL pattern
    # Add other URL patterns for the bookshelf app here
]
