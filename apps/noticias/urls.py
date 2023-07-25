from django.urls import path
from . import views
from django.contrib import admin

app_name = 'noticias'

# Urls de app noticias
urlpatterns = [

    path('', views.inicio, name="inicio"),

    path('<int:pk>', views.Contenido_Noticias, name='contenido'),
    path("admin/", admin.site.urls),
    path('comentario', views.Comentar_Noticia, name='comentar'),

    #barra busqueda
    path('busqueda/', views.busqueda, name='busqueda'),
]