# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView  # Import DetailView here
from .models import Library
from .models import Book

# Your function-based view for listing books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Get books related to the library
        return context
