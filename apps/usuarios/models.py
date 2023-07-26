from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios', default='user-default.jpg')

    def get_absolute_url(self):
        return reverse('index')