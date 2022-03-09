from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from api.serializers.bookmark_creation_serializer import BookmarkCreationSerializer
from api.serializers.bookmark_response_serializer import BookmarkResponseSerializer
from api.serializers.bookmark_update_serializer import BookmarkUpdateSerializer
from api.simple_authentication import SimpleAuthentication

from api.repositories.bookmark_repository import BookmarkRepository


class UnauthenticatedGet(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET']


class BookmarkView(APIView):

    authentication_classes = [SimpleAuthentication]
    permission_classes = [UnauthenticatedGet | IsAuthenticated]

    repository = BookmarkRepository()

    def get(self, request, bookmarkId):
        bookmark = self.repository.get_by_id(bookmarkId, request.user)
        if bookmark:
            serializer = BookmarkResponseSerializer(bookmark)
            return Response(data=serializer.data, status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = BookmarkCreationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )
        bookmark = self.repository.create(request.data, request.user)
        serializer = BookmarkResponseSerializer(bookmark)
        return Response(data=serializer.data, status=HTTP_201_CREATED)

    def delete(self, request, bookmarkId):
        deleted = self.repository.delete_by_id(bookmarkId, request.user)
        if deleted:
            return Response(status=HTTP_200_OK)
        else:
            return Response("Bookmark does not exist or does not exist for user", status=HTTP_404_NOT_FOUND)

    def patch(self, request, bookmarkId):
        serializer = BookmarkUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )
        bookmark = self.repository.update_by_id(bookmarkId, request.user, request.data)
        if bookmark:
            serializer = BookmarkResponseSerializer(bookmark)
            return Response(data=serializer.data, status=HTTP_200_OK)
        else:
            return Response("Bookmark does not exist or does not exist for user", status=HTTP_404_NOT_FOUND)
