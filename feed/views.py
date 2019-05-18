from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView

from feed.permissions import access_token_required
from feed.serializers import VoteSerializer, FeedSerializer, BookmarkSerializer


class Feed(APIView):
    http_method_names = ('get',)

    @access_token_required
    def get(self, request: Request, access_token: str):
        serializer = FeedSerializer(
            data={
                'feed_type': request.query_params.get('type')
            }, context={'access_token': access_token}
        )
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=HTTP_200_OK)


class Vote(APIView):
    http_method_names = ('post',)

    @access_token_required
    def post(self, request: Request, access_token: str):
        serializer = VoteSerializer(
            data=request.data, context={'access_token': access_token}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)


class Bookmark(APIView):
    http_method_names = ('post',)

    @access_token_required
    def post(self, request: Request, access_token: str):
        serializer = BookmarkSerializer(
            data=request.data, context={'access_token': access_token}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)
