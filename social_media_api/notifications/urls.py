from django.urls import path
from .views import notificationsListView, MarkAsReadView

urlpatterns = [
    path('', notificationsListView.as_view(), name='notification-list'),
    path('<int:pk>/mark-as-read/', MarkAsReadView.as_view(), name='mark-as-read'),
]