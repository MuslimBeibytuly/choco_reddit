from rest_framework import serializers

from authorization.models import access_token_from


class AccessTokenSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=256, required=True, write_only=True)
    access_token = serializers.SerializerMethodField(read_only=True)

    def get_access_token(self, validated_data):
        return access_token_from(validated_data['code'])
