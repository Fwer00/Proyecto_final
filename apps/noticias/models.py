from django.db import models
from django.utils import timezone

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
    categoria_noticia = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo

    
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)

    def __str__(self) -> str:
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()

