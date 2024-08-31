# Generated by Django 5.1 on 2024-08-31 18:49

import bazar.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("evento_inicio", models.CharField(max_length=5, null=True)),
                ("evento_fim", models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagem",
                    models.ImageField(
                        blank=True, upload_to=bazar.models.upload_image_item
                    ),
                ),
                ("descricao", models.CharField(max_length=200)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_usuario", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("senha", models.CharField(max_length=30)),
            ],
        ),
    ]
