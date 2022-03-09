from rest_framework import serializers


class BookmarkCreationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    url = serializers.URLField()
    is_public = serializers.BooleanField(default=True)
