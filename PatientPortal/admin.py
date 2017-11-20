# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import patient

# Register your models here.
class patientAdmin(admin.ModelAdmin):
	list_display = ['user','pid','fname','lname','phno','validated']

admin.site.register(patient,patientAdmin)