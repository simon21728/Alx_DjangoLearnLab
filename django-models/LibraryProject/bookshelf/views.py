from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
# Create your views here.

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

# views.py
# View for adding a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after adding a book
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View for editing a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after editing
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

# View for deleting a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion
    return render(request, 'delete_book.html', {'book': book})
