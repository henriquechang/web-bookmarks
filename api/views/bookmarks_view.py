from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api.serializers.bookmark_response_serializer import BookmarkResponseSerializer
from api.simple_authentication import SimpleAuthentication

from api.repositories.bookmark_repository import BookmarkRepository


class BookmarksView(APIView):

    authentication_classes = [SimpleAuthentication]

    repository = BookmarkRepository()

    def get(self, request):
        bookmarks = self.repository.get_all(request.user)
        return Response(data=[
            BookmarkResponseSerializer(bookmark).data
            for bookmark in bookmarks
        ], status=HTTP_200_OK)
