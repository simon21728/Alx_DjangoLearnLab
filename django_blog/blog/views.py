from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
# Create your views here.


@login_required
def profile(request):
    return render(request, 'blog/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('profile')  # Redirect to user profile
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
