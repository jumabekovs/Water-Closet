from django.db import models
from applications.advertisements.models import Advertisement


class Toilet(models.Model):
    address = models.JSONField()
    password = models.CharField(max_length=4)
    add = models.ForeignKey(Advertisement, related_name='toilets', on_delete=models.CASCADE)
