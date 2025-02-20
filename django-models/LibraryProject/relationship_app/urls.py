# relationship_app/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView 
urlpatterns = [
    # URL pattern for function-based view
    path('', list_books, name='list_books'),
    
    # URL pattern for class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Login URL using LoginView with custom template
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout URL using LogoutView with custom template
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Registration URL
    path('register/', views.register, name='register'),
]
