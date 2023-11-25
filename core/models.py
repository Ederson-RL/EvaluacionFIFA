from django.db import models

# Create your models here.
from django.contrib.auth.models import User


from django.db import models


class PlayingPosition(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')

    class Meta:
        verbose_name = 'Posición de Juego'
        verbose_name_plural = 'Posiciones de Juego'

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Nombre')
    last_name = models.CharField(max_length=30, verbose_name='Apellido')
    photo = models.ImageField(upload_to='players/',
                              verbose_name='Foto del jugador')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    position = models.ForeignKey(
        PlayingPosition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Posicion en la que juega'
    )

    jersey_number = models.PositiveIntegerField(
        verbose_name='Numero de jugador')
    is_starter = models.BooleanField(
        default=False, verbose_name='¿Es titular?')
    team = models.ForeignKey(
        'Team', on_delete=models.CASCADE, related_name='players', verbose_name='Equipo')

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Nuevo modelo para los roles de técnico


class TecnicoRol(models.Model):
    name = models.CharField(max_length=50, verbose_name='Rol')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'


class TecnicoNacionality(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Nombre de la Nacionalidad')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'


class Tecnico(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Nombre')
    last_name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name='Apellido')
    birth_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de nacimiento')
    rol = models.ForeignKey(
        TecnicoRol, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Rol')
    nacionalidad = models.ForeignKey(
        TecnicoNacionality, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Nacionalidad')

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        ordering = ['-id']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del equipo')
    flag = models.ImageField(upload_to='teams/flags/',
                             verbose_name='Imagen bandera')
    emblem = models.ImageField(
        upload_to='teams/emblems/', verbose_name='Emblema equipo')
    tecnico = models.OneToOneField(Tecnico, on_delete=models.CASCADE,
                                   related_name='equipo', verbose_name='Técnico del equipo', null=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.name
