from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ADMIN = 'ADMIN'
    SOCIO = 'SOCIO'
    ROLE_CHOICES = [
        (ADMIN, 'Administrador'),
        (SOCIO, 'Socio'),
    ]
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=SOCIO,
        verbose_name='Rol del usuario'
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def is_admin(self):
        return self.role == self.ADMIN

    def is_socio(self):
        return self.role == self.SOCIO
