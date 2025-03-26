from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [

    path('feed/', FeedView.as_view(), name='feed'),

    path('', include(router.urls)),
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