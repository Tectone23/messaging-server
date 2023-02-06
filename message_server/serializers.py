from django.contrib.auth.models import Group, User
from rest_framework import serializers

from message_server import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class UserBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserBundle
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"
