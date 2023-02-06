import json

from django.contrib.auth.models import User
from django.db import models


class UserBundle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identity_key = models.CharField("IdentityKey", max_length=255)
    pre_key = models.CharField("PreKey", max_length=255)
    pre_key_sig = models.CharField("PreKeySig", max_length=255)
    one_time_pre_key = models.TextField("OneTimePreKey")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_one_time_pre_key(self, x):
        self.one_time_pre_key = json.dumps(x)

    def get_one_time_pre_key(self):
        return json.loads(self.one_time_pre_key)


class Message(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_to_user"
    )
    message = models.TextField("Message Body")
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_from_user"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
