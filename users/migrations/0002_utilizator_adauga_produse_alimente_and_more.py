# Generated by Django 5.2.1 on 2025-05-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizator',
            name='adauga_produse_alimente',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilizator',
            name='face_rapoarte',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilizator',
            name='face_teste',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilizator',
            name='vede_produse_alimente',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilizator',
            name='vede_rapoarte',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilizator',
            name='vede_teste',
            field=models.BooleanField(default=False),
        ),
    ]
