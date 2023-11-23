from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# PERFIL DE USUARIO
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Apellido')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')

    # Opciones para el campo 'nacionalidad'
    NACIONALIDADES_CHOICES = [
        ('AR', 'Argentina'),
        ('BR', 'Brasil'),
        ('CO', 'Colombia'),
        # Agrega más opciones según sea necesario
    ]
    nacionalidad = models.CharField(max_length=2, choices=NACIONALIDADES_CHOICES, null=True, blank=True, verbose_name='Nacionalidad')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)