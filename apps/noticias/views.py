from django.shortcuts import render, HttpResponse
from .models import Noticia, Categoria
# Create your views here.

#Para cuando creemos el login
#from django.contrib.auth.decorators import login_required
#login_required
def inicio(request):
    contexto = {}
    id_categoria = request.GET.get('id', None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        n = Noticia.objects.all()  

    contexto['noticias'] = n

    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat

    return render(request, 'noticias/inicio.html', contexto)

#Para cuando creemos el login
#@login_required
def Contenido_Noticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)
    contexto['noticia'] = n

    return render(request, 'noticias/contenido.html', contexto)