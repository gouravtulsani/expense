# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.

class Expenses(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add = True)
	food_expense = models.CharField(max_length=100, blank=True)
	travelling_expense = models.CharField(max_length=100, blank=True)
	extra_expense = models.CharField(max_length=100, blank=True)




	def __str__(self):
		return (str(self.datetime))