from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows unauthenticated users to read, but not modify
    
    # Enabling filtering using DjangoFilterBackend
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    
    # Define filter fields: filter by title, author, and publication year
    filterset_fields = ['title', 'author', 'publication_date']
    
    # Enabling ordering: Allow ordering by title or publication date
    ordering_fields = ['title', 'publication_date']
    ordering = ['title']  # Default ordering
    
    # Enable searching by title and author
    search_fields = ['title', 'author']

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows unauthenticated users to read, but not modify

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books
