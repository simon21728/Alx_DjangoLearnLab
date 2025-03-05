# api/urls.py

from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
]
