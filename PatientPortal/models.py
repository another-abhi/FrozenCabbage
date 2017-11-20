from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.
class patient(models.Model):
        def __unicode__(self):
            return unicode(self.user)
        user=models.OneToOneField(User,on_delete=models.CASCADE)
        pid=models.UUIDField(default=uuid.uuid4, editable=False)
        fname=models.CharField(max_length=20)
        lname=models.CharField(max_length=20)
        phno=models.IntegerField(primary_key=True,max_length=20)
        validated=models.BooleanField(default=False)
        otp=models.IntegerField(default=0)

