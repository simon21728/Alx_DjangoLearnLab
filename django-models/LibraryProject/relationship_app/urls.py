# relationship_app/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
from .views import list_books, LibraryDetailView ,register
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
    path('register/', register(template_name='relationship_app/register.html'),name='register'),
    

    # urls.py
    path('admin_view/', views.admin_view(template_name='relationship_app/admin_view.html'),name='admin_view'),
    path('librarian_viw/', views.librarian_view(template_name='relationship_app/librarian_view.html'),name='librarian_view'),
    path('member_view/', views.member_view(template_name='relationship_app/member_view.html'), name='member_view'),

    path('add/', views.add_book(template_name='relationship_app/add_book.html'), name='add_book'),  # URL for adding a new book
    path('edit/<int:pk>/', views.edit_book(template_name='relationship_app/edit_book.html'),name='edit_book'),  # URL for editing a book
    path('delete/<int:pk>/', views.delete_book(template_name='relationship_app/delete_book.html'), name='delete_book'),  # URL for deleting a book
]
