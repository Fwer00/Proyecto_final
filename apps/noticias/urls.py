from django.urls import path
from . import views
from django.contrib import admin

app_name = 'noticias'

# Urls de app noticias
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.Inicio.as_view(), name="inicio"),
    path('<int:pk>/', views.Contenido_Noticias.as_view(), name='contenido'),
    path('comentario/', views.Comentar_Noticia, name='comentar'),
    path('comentario/delete/', views.Eliminar_Comentario, name='eliminar'),
    path('comentario/edit/<int:pk>/', views.Editar_ComentarioView.as_view(), name="editar"),

    #barra busqueda
    path('busqueda/', views.busqueda, name='busqueda'),
]