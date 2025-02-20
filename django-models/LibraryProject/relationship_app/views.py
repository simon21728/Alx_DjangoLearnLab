from django.shortcuts import render

# Create your views here.
from .models import Book
from .models import Library
from django.views.generic import DetailView
# Function-based view to list all books and their authors
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Override the get_context_data method to include all books in the library
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Get books related to the library
        return context