from django.shortcuts import render
from rest_framework import permissions
# Create your views here.
# api/views.py
from rest_framework.generics import ListAPIView
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer

# View to list all authors
class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer,

# View to get details of a single author (with nested books)
class AuthorDetailView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
# BookListCreateView: Handles listing all books and creating a new book.
class BookListCreateView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# BookDetailView: Handles retrieving, updating, or deleting a single book.
class BookDetailView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]