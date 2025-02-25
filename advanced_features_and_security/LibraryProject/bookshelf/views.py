from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
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

