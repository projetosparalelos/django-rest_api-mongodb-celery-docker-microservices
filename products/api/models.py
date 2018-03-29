# from django.db import models #comment out for sql
from djongo import models as models #for mongodb nosql

class Category(models.Model):
	name = models.CharField(max_length=100)


class Product(models.Model):
	category = models.IntegerField()
	name = models.CharField(max_length=100)
	price = models.FloatField()
	description = models.TextField()
