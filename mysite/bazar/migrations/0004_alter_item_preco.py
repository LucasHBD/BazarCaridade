# Generated by Django 5.1 on 2024-09-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bazar", "0003_item_evento_alter_evento_evento_fim_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="preco",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
