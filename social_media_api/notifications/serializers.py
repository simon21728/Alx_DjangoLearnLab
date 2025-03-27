from rest_framework import serializers
from .models import notification
from accounts.serializers import CustomUserSerializer

class notificationSerializer(serializers.ModelSerializer):
    actor = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = notification
        fields = ['id', 'actor', 'verb', 'target', 'read', 'created_at']
        read_only_fields = ['id', 'actor', 'verb', 'target', 'created_at']