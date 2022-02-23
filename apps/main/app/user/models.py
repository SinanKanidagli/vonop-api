from uuid import uuid4

from django.db import models
from project.models import Project


class User(models.Model):
    """User Model"""

    """
    *The reason for not using AbstractBaseUser or AbstractUser is there will be no password in User model
    """
    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    email: models.EmailField = models.EmailField(unique=True)
    project: models.ForeignKey = models.ForeignKey(Project, on_delete=models.CASCADE)
    extra_data: models.JSONField = models.JSONField(blank=True, null=True)
    is_staff: models.BooleanField = models.BooleanField(default=False)
    is_active: models.BooleanField = models.BooleanField(default=True)
    created: models.BooleanField = models.DateTimeField(auto_now_add=True)
    last_login: models.DateTimeField = models.DateTimeField(blank=True, null=True)

    class Meta:
        pass
