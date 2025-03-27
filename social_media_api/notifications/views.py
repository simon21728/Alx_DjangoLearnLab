from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer
from django.db.models import Q
# Create your views here.

class notificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

class MarkAsReadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        Notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
        Notification.read = True
        Notification.save()
        return Response({"status": "marked as read"})