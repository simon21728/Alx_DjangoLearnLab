from django.shortcuts import render

# Create your views here.
def some_function():
    from bookshelf.models import Book  # type: ignore # Import inside the function
    books = Book.objects.all()
    # Rest of the code