from django.urls import path

from feed.views import Feed, Vote, Bookmark

urlpatterns = (
    path('feed/', Feed.as_view()),
    path('vote/', Vote.as_view()),
    path('bookmark/', Bookmark.as_view()),
)
