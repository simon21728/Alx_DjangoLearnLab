# relationship_app/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
from .views import list_books, LibraryDetailView ,register,add_book,edit_book
urlpatterns = [
    # URL pattern for function-based view
    path('', list_books, name='list_books'),
    
    # URL pattern for class-based view
    path('', views.LibraryDetailView.as_view(), name='library_detail'),

    # Login URL using LoginView with custom template
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout URL using LogoutView with custom template
    path('', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Registration URL
    path('register/', views.register,name='register'),
    

    # urls.py
    path('admin_view/', views.admin_view,name='admin_view'),
    path('librarian_view/', views.librarian_view,name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),

    path('add_book/', add_book, name='add_book'),  # URL for adding a new book
    path('edit_book/<int:pk>/', edit_book,name='edit_book'),  # URL for editing a book
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),  # URL for deleting a book
]
