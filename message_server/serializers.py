import base64

from django.contrib.auth.models import Group, User
from rest_framework import serializers

from message_server import models
from django.db import models as dmodels



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class MyBinaryField(serializers.Field):
    def to_internal_value(self, obj):
        print(obj)
        return obj.encode('ISO-8859-1')

    def to_representation(self, value):
        if isinstance(value, str):
            return value.encode('ISO-8859-1')
        return value.decode('ISO-8859-1')


class UserBundleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    serializer_field_mapping = (
        serializers.ModelSerializer.serializer_field_mapping.copy()
    )
    serializer_field_mapping[dmodels.BinaryField] = MyBinaryField

    identity_key = MyBinaryField()
    pre_key = MyBinaryField()
    pre_key_sig = MyBinaryField()
    one_time_pre_key = MyBinaryField()

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
    serializer_field_mapping = (
        serializers.ModelSerializer.serializer_field_mapping.copy()
    )
    serializer_field_mapping[dmodels.BinaryField] = MyBinaryField

    message = MyBinaryField()

    class Meta:
        model = models.Message
        fields = "__all__"
