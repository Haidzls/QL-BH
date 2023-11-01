from django.db import models

class Product(models.Model):
  thumbnail = models.CharField(max_length=255)
  shortDescription = models.CharField(max_length=100)
  slkbd = models.IntegerField(default=0)
  slk = models.IntegerField(default=0)
  slb = models.IntegerField(default=0)
  gianhap = models.IntegerField(default=0)
  giaban = models.IntegerField(default=0)
  category = models.CharField(max_length=50)

