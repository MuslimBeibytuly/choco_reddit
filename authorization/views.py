from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authorization.serializers import AccessTokenSerializer
from feed.models import RedditClient
from feed.permissions import access_token_required


class AccessToken(APIView):
    http_method_names = ('get',)
    permission_classes = (AllowAny,)

    def get(self, request: Request):
        serializer = AccessTokenSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)


class Profile(APIView):
    http_method_names = ('get',)

    @access_token_required
    def get(self, request, access_token: str):
        return Response(data={
            'user_info': RedditClient(access_token=access_token).user_info
        })
