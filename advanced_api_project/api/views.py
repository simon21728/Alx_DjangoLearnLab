from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing or retrieving authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing or retrieving books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
