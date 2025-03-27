from django.urls import path
from .views import notificationListView, MarkAsReadView

urlpatterns = [
    path('', notificationListView.as_view(), name='notification-list'),
    path('<int:pk>/mark-as-read/', MarkAsReadView.as_view(), name='mark-as-read'),
]