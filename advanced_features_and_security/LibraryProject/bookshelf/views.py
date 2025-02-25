from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
def book_list(request):
    """
    View to list all books in the system.
    """
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})
# View to create a book
@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle book creation logic here
        pass
    return render(request, 'create_book.html')

# View to edit a book
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle book editing logic here
        pass
    return render(request, 'edit_book.html', {'book': book})

# View to view a book
@permission_required('relationship_app.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def index(request):
    return HttpResponse("Welcome to the Bookshelf app!")
# bookshelf/views.py


# Function to check if the user has 'Admin' role
def is_admin(user):
    return user.userprofile.role == 'Admin'  # Assuming you are using the UserProfile model for roles

# Admin view that only Admin users can access
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin page!")

