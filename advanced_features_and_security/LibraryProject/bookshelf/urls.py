# bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # Example URL pattern
    path('admin/', views.admin_view, name='admin_view'),  # Add the URL for the Admin view
    path('add_book/', views.add_book, name='add_book'),
]
