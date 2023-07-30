from django.contrib.auth.models import Group, Permission
from .models import Usuario
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Usuario)
def add_user_to_miembro_group(sender, instance:Usuario, created, **kwargs):
    if created:
        try:
            miembros = Group.objects.get(name='Miembro')
        except Group.DoesNotExist:
            colaboradores = Group.objects.create(name='Colaborador')
            miembros = Group.objects.create(name='Miembro')
            ct = ContentType.objects.get_for_model(Usuario)
            perm1 = Permission.objects.create(codename="delete_comment", name='Can delete comment', content_type=ct)
            perm2 = Permission.objects.create(codename="change_comment", name='Can change comment', content_type=ct)
            perm3 = Permission.objects.create(codename="add_categoria", name='Can add categoria', content_type=ct)
            perm4 = Permission.objects.create(codename="add_noticia", name='Can add noticia', content_type=ct)
            perm5 = Permission.objects.create(codename="change_noticia", name='Can change noticia', content_type=ct)
            perm6 = Permission.objects.create(codename="delete_noticia", name='Can delete noticia', content_type=ct)
            colaboradores.permissions.add(perm1, perm2, perm3, perm4, perm5, perm6)
            miembros.permissions.add(perm1, perm2)
        instance.groups.add(miembros)
