import base64
import json

from django.contrib.auth.models import User
from django.db import models


class UserBundle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identity_key = models.BinaryField("IdentityKey")
    pre_key = models.BinaryField("PreKey")
    pre_key_sig = models.BinaryField("PreKeySig")
    one_time_pre_key = models.BinaryField("OneTimePreKey")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_to_user"
    )
    message = models.BinaryField("Message Body")
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_from_user"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message_read_at = models.DateTimeField(null=True)


# Create your models here.
