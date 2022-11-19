from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    spot = models.ForeignKey('spots.spot', on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='people')
