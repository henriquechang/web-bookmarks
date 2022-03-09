from django.urls import path

from api.views.bookmark_view import BookmarkView
from api.views.bookmarks_view import BookmarksView
from api.views.home_view import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('bookmark', BookmarkView.as_view()),
    path('bookmark/<int:bookmarkId>', BookmarkView.as_view()),
    path('bookmarks', BookmarksView.as_view())
]