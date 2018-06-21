# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Result(models.Model):

	created_date = models.DateTimeField(default=timezone.now, editable=False)
	hostname = models.CharField(max_length=255)
	ip = models.GenericIPAddressField()
	ua = models.CharField(max_length=255)
	lang = models.CharField(max_length=255)
	dl = models.CharField(max_length=255, blank=True, null=True)
	ul = models.CharField(max_length=255, blank=True, null=True)
	ping = models.CharField(max_length=255, blank=True, null=True)
	jitter = models.CharField(max_length=255, blank=True, null=True)
	log = models.TextField(max_length=65535, blank=True, null=True)

	def __str__(self):
		return "%s %s" % (self.ip, self.hostname)