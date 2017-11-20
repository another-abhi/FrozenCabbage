# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-19 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('PatientPortal', '0005_auto_20171119_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
