from rest_framework import serializers
from .models import Notification
from accounts.serializers import CustomUserSerializer

class NotificationSerializer(serializers.ModelSerializer):
    actor = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'read', 'created_at']
        read_only_fields = ['id', 'actor', 'verb', 'target', 'created_at']