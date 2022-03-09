import logging

from django.db.models import Q
from django.utils.timezone import now

from api.models.bookmark import Bookmark


class BookmarkRepository:

    __logger = logging.getLogger(__name__)

    def create(self, data, user):
        bookmark = Bookmark(
            title=data.get('title'),
            url=data.get('url'),
            is_public=data.get('isPublic'),
            owner=user
        )
        bookmark.save()
        return bookmark

    def delete_by_id(self, id: int, user):
        try:
            bookmark = Bookmark.objects.get(id=id, owner=user)
            bookmark.delete()
            return True
        except Exception as e:
            self.__logger.error(e)
            return False

    def update_by_id(self, id: int, user, filters):
        try:
            bookmark = Bookmark.objects.get(id=id, owner=user)
            if filters.get('title'):
                bookmark.title = filters.get('title')
            if filters.get('url'):
                bookmark.url = filters.get('url')
            if filters.get('isPublic') is not None:
                bookmark.is_public = filters.get('isPublic')
            bookmark.updated_at = now()
            bookmark.save()
            return bookmark
        except Exception as e:
            self.__logger.error(e)

    def get_by_id(self, id: int, user):
        try:
            if not user.is_anonymous:
                bookmark = Bookmark.objects.get(Q(owner=user) | Q(is_public=True), id=id)
            else:
                bookmark = Bookmark.objects.get(id=id, is_public=True)
            return bookmark
        except Exception as e:
            self.__logger.error(e)

    def get_all(self, user):
        try:
            if not user.is_anonymous:
                bookmarks = Bookmark.objects.filter(Q(owner=user) | Q(is_public=True))
            else:
                bookmarks = Bookmark.objects.filter(is_public=True)
            return bookmarks.all()
        except Exception as e:
            self.__logger.error(e)
