from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    path('posts/', views.PostListView.as_view(), name='post-list'),
    path("posts/new/", views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name='post-edit'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post-delete'),
]
