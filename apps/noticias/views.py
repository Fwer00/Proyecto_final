from django.shortcuts import render, HttpResponse, redirect
from .models import Noticia, Categoria, Comentario

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.

#Para cuando creemos el login
#from django.contrib.auth.decorators import login_required
#@login_required
def inicio(request):
    contexto = {}
    id_categoria = request.GET.get('id', None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        n = Noticia.objects.all()  

    contexto['noticias'] = n

    cate = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cate

    return render(request, 'noticias/inicio.html', contexto)

#Para cuando creemos el login
#@login_required
def Contenido_Noticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)
    contexto['noticia'] = n

    c = Comentario.objects.filter(noticia=n)
    contexto['comentarios'] = c

    return render(request, 'noticias/contenido.html', contexto)


#@login_required
def Comentar_Noticia(request):
    comentario = request.POST.get('comentario', None)
    #user = request.user
    noti = request.POST.get('id_noticia', None)
    noticia = Noticia.objects.get(pk=noti)
    coment = Comentario.objects.create(
         noticia=noticia, texto=comentario)
    return redirect(reverse_lazy('noticias:contenido', kwargs={"pk": noti}))
# falta en coment (usuario=user)


#BRRA BUSQUEDA
def busqueda(request):
    if request.method == "POST":
        busquedaa = request.POST['busquedaa']
        resultados = Noticia.objects.filter(titulo__contains=busquedaa)

        return render(request, 'busqueda.html', {'busquedaa':busquedaa,
                                                 'resultados': resultados})
    else:
        return render(request, 'busqueda.html', {})