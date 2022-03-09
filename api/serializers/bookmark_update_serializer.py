from rest_framework import serializers


class BookmarkUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    url = serializers.URLField(required=False)
    is_public = serializers.BooleanField(default=True, required=False)
