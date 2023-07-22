from django.db import models

# Create your models here.

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, )
    correo = models.EmailField()
    mensaje = models.TextField()

    def _str_(self):
        return self.nombre