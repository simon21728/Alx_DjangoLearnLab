from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer

# View to list all authors
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# View to get details of a single author (with nested books)
class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
