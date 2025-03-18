from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name='post-edit'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post-delete'),
    #path('post/new/', views.post_create, name='post_create'),  # Create a new post
    #path('post/<int:pk>/update/', views.post_update, name='post_update'),  # Update an existing pos

    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name='comment-create'),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name='comment-updatet'),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name='comment-delete'),

    
    # Tagging and search functionality
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post_by_tag'),  # URL for posts by tag
    path('tags/<str:tag_name>/', views.tag_posts, name='tag-posts'),
    path('search/', views.search, name='search'),
]
