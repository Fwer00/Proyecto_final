from django.shortcuts import render, HttpResponse, redirect
from .models import Noticia, Categoria, Comentario
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from .forms import ComentarioForm


class Inicio(View):
    def get(self, request, *args, **kwargs):
        id_categoria = request.GET.get('id', None)
        if id_categoria:
            n = Noticia.objects.filter(categoria_noticia=id_categoria)
        else:
            n = Noticia.objects.all() 

        cate = Categoria.objects.all().order_by('nombre')
        contexto = {
            'noticias':n,
            'categorias': cate,
        }
        return render(request, 'noticias/inicio.html', contexto)


class Contenido_Noticias(View):
    def get(self, request, pk, *args, **kwargs):
        noticia = Noticia.objects.get(pk=pk)
        comentarios = Comentario.objects.filter(noticia=noticia).order_by('-fecha')

        contexto = {
            'noticia':noticia,
            'comentarios':comentarios,
        }
        return render(request, 'noticias/contenido.html', contexto)
    
    def noticia(self, request, pk, *args, **kwargs):
        noticia = Noticia.objects.get(pk=pk)

        comentarios = Comentario.objects.filter(noticia=noticia).order_by('-fecha')
        contexto = {
            'noticia':noticia,
            'comentarios':comentarios,
        }
        return render(request, 'noticias/contenido.html', contexto)
    

class Editar_ComentarioView(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'noticias/edicion.html'








    
def Eliminar_Comentario(request):
    user = request.user
    noti = request.POST.get('noticia_id', None)
    Comentario.objects.filter(usuario_id=user).delete()
    return redirect(reverse_lazy('noticias:inicio'))

def Comentar_Noticia(request):
    comentario = request.POST.get('comentario', None)
    user = request.user
    noti = request.POST.get('id_noticia', None)
    noticia = Noticia.objects.get(pk=noti)
    coment = Comentario.objects.create(
         usuario=user ,noticia=noticia, texto=comentario)
    return redirect(reverse_lazy('noticias:contenido', kwargs={"pk": noti}))



#BRRA BUSQUEDA
def busqueda(request):
    if request.method == "POST":
        busquedaa = request.POST['busquedaa']
        resultados = Noticia.objects.filter(titulo__contains=busquedaa)

        return render(request, 'busqueda.html', {'busquedaa':busquedaa,
                                                 'resultados': resultados})
    else:
        return render(request, 'busqueda.html', {})