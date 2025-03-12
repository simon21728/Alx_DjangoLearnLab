from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters

# List all books and create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated user
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']  # Allow searching by title or author name
    def perform_create(self, serializer):
        # Custom logic before saving the book instance
        serializer.save()

# Retrieve, update, or delete a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users