# api/urls.py
from django.urls import path
from .views import AuthorListView, AuthorDetailView

urlpatterns = [
    # Endpoint to retrieve a list of authors
    path('authors/', AuthorListView.as_view(), name='author-list'),
    
    # Endpoint to retrieve a single author with their books
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
