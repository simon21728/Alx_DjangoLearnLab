from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,LikePostView, UnlikePostView
from .views import FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [

    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
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