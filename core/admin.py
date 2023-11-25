from django.contrib import admin
from .models import PlayingPosition, Player, Tecnico, Team, TecnicoRol, TecnicoNacionality


# Register your rrwdels here.
from import_export.admin import ImportExportModelAdmin


@admin.register(PlayingPosition)
class PlayingPositionAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date',
                    'position', 'jersey_number', 'is_starter', 'team')
    list_filter = ('team', 'is_starter', 'position')
    search_fields = ('first_name', 'last_name')


@admin.register(Tecnico)
class TecnicoAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name',
                    'birth_date', 'nacionalidad', 'rol')
    list_filter = ('nacionalidad', 'rol')
    search_fields = ('first_name', 'last_name')


@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    list_display = ('name', 'tecnico')
    search_fields = ('name',)


# Clase de administración para TecnicoRol
@admin.register(TecnicoRol)
class TecnicoRolAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Clase de administración para TecnicoNacionalidad


@admin.register(TecnicoNacionality)
class TecnicoNacionalidadAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
