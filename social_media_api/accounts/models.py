from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # Custom fields
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='followers'
    )
    
    # Fix for groups and permissions conflicts
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name="custom_user_set",  # Unique related_name
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="custom_user_set",  # Unique related_name
        related_query_name="custom_user",
    )
    
    class Meta:
        # Ensure this model is not considered for migrations by Django's auth app
        default_permissions = ()
    
    def __str__(self):
        return self.username