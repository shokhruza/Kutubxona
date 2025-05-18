from django.contrib.auth.models import AbstractUser
from django.db import models

class RoleChoices(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrator'
    OPERATOR = 'OPERATOR', 'Operator'
    CLIENT = 'CLIENT', 'Client'

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    def __str__(self):
        return self.username
