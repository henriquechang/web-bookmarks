from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Bookmark(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    owner = models.ForeignKey(User, related_name='bookmark', on_delete=models.CASCADE)
