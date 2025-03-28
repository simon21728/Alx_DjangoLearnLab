from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    UserProfileView
)
from .views import (
    FollowUserView,
    UnfollowUserView,
    FollowingListView,
    FollowersListView
)

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('following/', FollowingListView.as_view(), name='following-list'),
    path('followers/', FollowersListView.as_view(), name='followers-list'),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]