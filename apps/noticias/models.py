from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from apps.usuarios.models import Usuario
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=45, null=False)
    resumen = models.CharField(max_length=100, null=False)
    cuerpo = models.TextField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias', null=True)
    categoria_noticia = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)

    #class Meta:
    #   ordering = ('-fecha',)

    def __str__(self) -> str:
        return self.titulo

    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()


class Comentario(models.Model):
    texto = models.TextField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=510)

    def __str__(self) -> str:
        return f"{self.noticia} {self.texto}"
    
    def get_absolute_url(self):
        return reverse('noticias:inicio')

