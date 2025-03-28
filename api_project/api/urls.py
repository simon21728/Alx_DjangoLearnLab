# api/urls.py

from django.urls import path,include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', include(router.urls)),  # This will automatically create routes for all CRUD operations
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
