from functools import wraps

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class HasAccessToken(BasePermission):
    message = 'No access token'

    def has_permission(self, request: Request, view):
        return request.META.get('HTTP_AUTHORIZATION') is not None


def access_token_required(view):
    @wraps(view)
    def wrapper(self, request: Request):
        access_token = request.META.get('HTTP_AUTHORIZATION')
        if access_token is None:
            raise AuthenticationFailed(detail='No access token')
        return view(self, request, access_token)

    return wrapper
