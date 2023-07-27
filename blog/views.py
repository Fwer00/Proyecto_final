from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def personajes(request):
    return render(request, 'personajes\personajes.html')

def guerrero(request):
    return render(request, 'personajes\guerrero.html')

def ranger(request):
    return render(request, 'personajes/ranger.html')

def hechicera(request):
    return render(request, 'personajes\hechicera.html')

def gigante(request):
    return render(request, 'personajes\gigante.html')

def domadora(request):
    return render(request, 'personajes\domadora.html')

def musa(request):
    return render(request, 'personajes\musa.html')

def maehwa(request):
    return render(request, 'personajes\maehwa.html')

def valquiria(request):
    return render(request, 'personajes/valquiria.html')

def kunoichi(request):
    return render(request, 'personajes\kunoichi.html')

def ninja(request):
    return render(request, 'personajes/ninja.html')

def mago(request):
    return render(request, 'personajes\mago.html')

def bruja(request):
    return render(request, 'personajes/bruja.html')

def mystic(request):
    return render(request, 'personajes\mystic.html')

def striker(request):
    return render(request, 'personajes\striker.html')

def lahn(request):
    return render(request, 'personajes\lahn.html')

def arquero(request):
    return render(request, 'personajes/arquero.html')

def dark_knight(request):
    return render(request, 'personajes\dark_knight.html')

def shai(request):
    return render(request, 'personajes\shai.html')

def guardiana(request):
    return render(request, 'personajes\guardiana.html')

def hashashin(request):
    return render(request, 'personajes\hashashin.html')

def nova(request):
    return render(request, 'personajes/nova.html')

def sage(request):
    return render(request, 'personajes\sage.html')

def corsair(request):
    return render(request, 'personajes\corsair.html')

def drakania(request):
    return render(request, 'personajes\drakania.html')

def wusa(request):
    return render(request, 'personajes\wusa.html')

def maegu(request):
    return render(request, 'personajes\maegu.html')

def mapa(request):
    return render(request, 'mapa\mapa_interactivo.html')

