from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import*
# Create your models here.

class notifications(models.Model):
    recipient = models.ForeignKey(custom_user, related_name='received_notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(custom_user, on_delete=models.CASCADE,related_name='acted_notifications')
    verb = models.CharField(max_length=255)  # e.g., "liked your post", "started following you"
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.actor.username} {self.verb}"