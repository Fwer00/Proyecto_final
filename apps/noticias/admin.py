from django.contrib import admin
from .models import Categoria, Noticia

# Register your models here.
#@admin.register(Noticia)
#class NoticiaAdmin(admin,ModelAdmin):
    #list_display = ()
admin.site.register(Categoria)
admin.site.register(Noticia)

