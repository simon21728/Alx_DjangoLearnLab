from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import notification
from .serializers import notificationsSerializer
from django.db.models import Q
# Create your views here.

class notificationListView(generics.ListAPIView):
    serializer_class = notificationsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return notification.objects.filter(recipient=self.request.user).order_by('-created_at')

class MarkAsReadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        notification = get_object_or_404(notification, pk=pk, recipient=request.user)
        notification.read = True
        notification.save()
        return Response({"status": "marked as read"})