from django.db import models
from django.contrib.auth import get_user_model


class Spot(models.Model):
    continent = models.CharField(max_length=256)
    x = models.IntegerField()
    y = models.IntegerField()
