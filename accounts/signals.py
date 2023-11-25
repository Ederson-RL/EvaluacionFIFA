# from django.contrib.auth.models import Group
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import Profile


# @receiver(post_save, sender=Profile)
# def add_user_to_asistente_group(sender, instance, created, **kwargs):
#     if created:
#         try:
#             rols = Group.objects.get(name='asistente')
#         except Group.DoesNotExist:
#             rols = Group.objects.create(name='asistente')
#             rols = Group.objects.create(name='técnico')
#             rols = Group.objects.create(name='médico')
#             rols = Group.objects.create(name='preparador')
#         instance.user.groups.add(rols)
