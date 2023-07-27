from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProfilePictureForm



class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        form.save()

        return redirect('apps.usuarios:login')
    
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('index')

class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Cerrado de sesión exitoso.')

        return reverse('apps.usuarios:login')


def edit_profile(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('apps.usuarios:perfil')
    else:
        form = ProfilePictureForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form' : form})


@login_required
def perfil(request):
    return render(request, 'registration/perfil.html')


