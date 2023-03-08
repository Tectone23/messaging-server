from django.contrib.auth.models import Group, User

# from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework import filters
from message_server.models import Message, UserBundle
from message_server.serializers import GroupSerializer, UserSerializer, UserBundleSerializer, MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    search_fields = ['username', 'email']
    filterset_fields = [field.name for field in User._meta.fields]
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserBundleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserBundle.objects.all()
    serializer_class = UserBundleSerializer
    filterset_fields = ['user']
    # permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filterset_fields = [field.name for field in Message._meta.fields if field.name != 'message']
    # permission_classes = [permissions.IsAuthenticated]
