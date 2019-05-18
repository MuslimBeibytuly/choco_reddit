from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from feed.models import RedditClient


class FeedSerializer(serializers.Serializer):
    feed = serializers.SerializerMethodField(read_only=True)
    feed_type = serializers.CharField(write_only=True, allow_null=True)

    def get_feed(self, validated_data):
        client = RedditClient(access_token=self.context['access_token'])
        try:
            return client.feed(**validated_data)
        except ObjectDoesNotExist:
            raise ValidationError(detail='Invalid feed type')


class VoteSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=256, required=True, write_only=True)
    dir = serializers.IntegerField(min_value=-1, max_value=1, required=True, write_only=True)
    rank = serializers.IntegerField(min_value=1, default=1, write_only=True)

    def save(self):
        self.validated_data['action'] = 'vote'
        client = RedditClient(access_token=self.context['access_token'])
        client.act(**self.validated_data)


class BookmarkSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=256, required=True, write_only=True)
    category = serializers.CharField(max_length=256, required=False, write_only=True)
    bookmark = serializers.BooleanField(default=True, write_only=True)

    def save(self):
        self.validated_data['action'] = 'save' if self.validated_data.pop('bookmark') else 'unsave'
        client = RedditClient(access_token=self.context['access_token'])
        client.act(**self.validated_data)
