from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilizator(AbstractUser):
    ROL = (
        ('admin', 'Administrator'),
        ('user', 'Utilizator'),
    )
    rol = models.CharField(max_length=10, choices=ROL, default='user')

    def __str__(self):
        return f"{self.username} ({self.rol})"
