from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios', default='usuarios/user-default.png')

    def get_absolute_url(self):
        return reverse('index')