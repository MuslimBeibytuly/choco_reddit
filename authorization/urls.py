from django.urls import path

from authorization.views import AccessToken, Profile

urlpatterns = (
    path('access_token/', AccessToken.as_view()),
    path('profile/', Profile.as_view()),
)
