from django.shortcuts import render
from .forms import ContactoForm

from django.core.mail import send_mail
from django.conf import settings

#CORREO HTML
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def contacto(request):
    data = {
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            correo = formulario.cleaned_data['correo']
            mensaje = formulario.cleaned_data['mensaje']

            # send_mail(correo, mensaje, 'settings.EMAIL_HOST_USER', ['jugadoresdeldesiertoblog@gmail.com'], fail_silently=False)

            # formulario.save()
            # data["mensaje"] = "Consulta enviada"

            html_content = render_to_string("correo_template.html", {'nombre': nombre, 'correo': correo, 'mensaje': mensaje})
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                "CONTACTO DESDE EL BLOG",
                text_content,
                'settings.EMAIL.HOST.USER',
                ['jugadoresdeldesiertoblog@gmail.com']
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            return render(request, 'contacto.html', data)
        else:
            data["form"] = formulario

    return render(request, 'contacto.html', data)