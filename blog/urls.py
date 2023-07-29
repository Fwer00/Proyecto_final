"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('apps.contacto.urls')),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', include('apps.noticias.urls')),
    path('', include('apps.usuarios.urls')),
    path('', include('django.contrib.auth.urls')),
    path('personajes/', views.personajes, name='personajes'),
    path('guerrero/', views.guerrero, name='guerrero'),
    path('ranger/', views.ranger, name='ranger'),
    path('hechicera/', views.hechicera, name='hechicera'),
    path('gigante/', views.gigante, name='gigante'),
    path('domadora/', views.domadora, name='domadora'),
    path('musa/', views.musa, name='musa'),
    path('maehwa/', views.maehwa, name='maehwa'),
    path('valquiria/', views.valquiria, name='valquiria'),
    path('kunoichi/', views.kunoichi, name='kunoichi'),
    path('ninja/', views.ninja, name='ninja'),
    path('mago/', views.mago, name='mago'),
    path('bruja/', views.bruja, name='bruja'),
    path('mystic/', views.mystic, name='mystic'),
    path('striker/', views.striker, name='striker'),
    path('lahn/', views.lahn, name='lahn'),
    path('arquero/', views.arquero, name='arquero'),
    path('dark_knight/', views.dark_knight, name='dark_knight'),
    path('shai/', views.shai, name='shai'),
    path('guardiana/', views.guardiana, name='guardiana'),
    path('hashashin/', views.hashashin, name='hashashin'),
    path('nova/', views.nova, name='nova'),
    path('sage/', views.sage, name='sage'),
    path('corsair/', views.corsair, name='corsair'),
    path('drakania/', views.drakania, name='drakania'),
    path('wusa/', views.wusa, name='wusa'),
    path('maegu/', views.maegu, name='maegu'),
    path('mapa/', views.mapa, name='mapa'),
    path('nosotros/',views.nosotros, name='nosostros'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
