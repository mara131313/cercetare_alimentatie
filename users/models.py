from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilizator(AbstractUser):
    ROL = (
        ('admin', 'Administrator'),
        ('user', 'Utilizator'),
    )
    rol = models.CharField(max_length=10, choices=ROL, default='user')

    #PERMISIUNI
    vede_rapoarte = models.BooleanField(default=True)
    face_rapoarte = models.BooleanField(default=True)
    vede_produse_alimente = models.BooleanField(default=False)
    adauga_produse_alimente = models.BooleanField(default=False)
    vede_teste = models.BooleanField(default=False)
    face_teste = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.rol})"

class AuditLog(models.Model):
    user = models.ForeignKey(Utilizator, on_delete=models.SET_NULL, null=True)
    actiune = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp}] {self.user} - {self.actiune}"