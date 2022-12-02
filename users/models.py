from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    spot = models.ForeignKey('spots.spot', on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='people')
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=12, unique=True)
