from django.shortcuts import render
from rest_framework import permissions
# Create your views here.
# api/views.py
from rest_framework import generics
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer

# View to list all authors
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer,

# View to get details of a single author (with nested books)
class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
# BookListCreateView: Handles listing all books and creating a new book.
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# BookDetailView: Handles retrieving, updating, or deleting a single book.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]