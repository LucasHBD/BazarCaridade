# Generated by Django 4.2.11 on 2024-09-18 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bazar", "0006_remove_item_evento_item_evento"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="evento",
        ),
        migrations.AddField(
            model_name="item",
            name="evento",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="bazar.evento",
            ),
        ),
    ]
