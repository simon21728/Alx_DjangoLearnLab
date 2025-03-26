from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import (
    UserRegisterView,
    UserLoginView,
    UserProfileView
)
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),



    path('posts/<int:post_pk>/comments/', 
         CommentViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }), name='post-comments'),
    path('posts/<int:post_pk>/comments/<int:pk>/', 
         CommentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }), name='comment-detail'),
]