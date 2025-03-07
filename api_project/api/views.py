from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
# BookViewSet handles CRUD operations automatically
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieves all books
    serializer_class = BookSerializer  # Serializer to convert Book model instances to JSON
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access this view


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to format the response
