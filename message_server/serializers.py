from django.contrib.auth.models import Group, User
from rest_framework import serializers

from message_server import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class UserBundleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.UserBundle
        fields = [
            "id",
            "user",
            "identity_key",
            "pre_key",
            "pre_key_sig",
            "one_time_pre_key",
            "created_at",
            "updated_at",
            "username"
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"
