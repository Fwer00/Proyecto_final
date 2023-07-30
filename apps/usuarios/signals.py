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
            miembros.permissions.add(perm1, perm2)
        instance.groups.add(miembros)
