from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for listing all books and creating a new book
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    # Endpoint for retrieving, updating, or deleting a single book
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]