from django.utils.timezone import now
from rest_framework import serializers


class BookmarkResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    url = serializers.URLField()
    is_public = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(default=now)
    updated_at = serializers.DateTimeField(default=now)
