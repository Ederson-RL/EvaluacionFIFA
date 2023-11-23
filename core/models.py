from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class PlayingPosition(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Posición de Juego'
        verbose_name_plural = 'Posiciones de Juego'
        ordering = ['nombre']
    
    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    photo = models.ImageField(upload_to='players/', verbose_name='Player Photo')
    birth_date = models.DateField(verbose_name='Birth Date')
    position = models.ForeignKey(PlayingPosition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Playing Position')
    jersey_number = models.PositiveIntegerField(verbose_name='Jersey Number')
    is_starter = models.BooleanField(default=False, verbose_name='Is Starter?')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='players', verbose_name='Team')

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Team Name')
    flag = models.ImageField(upload_to='teams/flags/', verbose_name='Flag Image')
    emblem = models.ImageField(upload_to='teams/emblems/', verbose_name='Team Emblem')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='equipo', verbose_name='Usuario del equipo')
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['nombre']

    def __str__(self):
        return self.name
