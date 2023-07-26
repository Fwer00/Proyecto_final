from django.urls import path
from . import views
from .views import LoginUsuario
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth

app_name = 'apps.usuarios'

urlpatterns = [
    path('registrar/', views.RegistrarUsuario.as_view(), name='registrar'),
    path('login/', auth.LoginView.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar/', views.edit_profile, name = 'editar_perfil'),
]
