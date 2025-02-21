# bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # Example URL pattern
    path('admin/', views.admin_view, name='admin_view'),  # Add the URL for the Admin view

    
    path('add/', views.add_book, name='add_book'),  # URL for adding a new book
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),  # URL for editing a book
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),  # URL for deleting a book
]
