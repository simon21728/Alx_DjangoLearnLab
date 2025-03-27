from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone



from django.contrib.contenttypes.models import ContentType

User = get_user_model()
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Return all posts by default, but can be filtered
        return Post.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                {"detail": "You do not have permission to delete this post."},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                {"detail": "You do not have permission to edit this post."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # This includes Comment.objects.all() for the base queryset
        queryset = Comment.objects.all()
        post_pk = self.kwargs.get('post_pk')
        if post_pk:
            queryset = queryset.filter(post_id=post_pk)
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                {"detail": "You do not have permission to delete this comment."},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                {"detail": "You do not have permission to edit this comment."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)
    
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Get posts from users the current user is following
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Explicitly using get_object_or_404 through generics
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Explicit Like.objects.get_or_create with both conditions
        Like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response(
                {"error": "You have already liked this post"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create notification if it's not the user's own post
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
                timestamp=timezone.now()
            )
        
        return Response(
            {
                "message": "Post liked successfully",
                "likes_count": post.likes.count()
            },
            status=status.HTTP_201_CREATED
        )

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = generics.get_object_or_404(Like, user=request.user, post=post)
        like.delete()
        
        return Response(
            {
                "message": "Post unliked successfully",
                "likes_count": post.likes.count()
            },
            status=status.HTTP_200_OK
        )