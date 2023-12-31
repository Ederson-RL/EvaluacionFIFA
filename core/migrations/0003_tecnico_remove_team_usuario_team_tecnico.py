# Generated by Django 4.2.7 on 2023-11-23 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_player_options_alter_playingposition_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Apellido')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('nacionalidad', models.CharField(blank=True, choices=[('AR', 'Argentina'), ('BR', 'Brasil'), ('CO', 'Colombia')], max_length=2, null=True, verbose_name='Nacionalidad')),
                ('rol', models.CharField(blank=True, choices=[('TE', 'Técnico'), ('AS', 'Asistente'), ('ME', 'Médico'), ('PR', 'Preparador')], max_length=2, null=True, verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='team',
            name='usuario',
        ),
        migrations.AddField(
            model_name='team',
            name='tecnico',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipo', to='core.tecnico', verbose_name='Técnico del equipo'),
        ),
    ]
