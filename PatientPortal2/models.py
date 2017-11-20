from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class patient(models.Model):
        def __unicode__(self):
            return unicode(self.user)
        user=models.OneToOneField(User,on_delete=models.CASCADE)
        pid=models.IntegerField()
        fname=models.CharField(max_length=20)
        lname=models.CharField(max_length=20)
        phno=models.IntegerField(max_length=10)
        validated=models.BooleanField(default=False)
        age=models.IntegerField()
