# Generated by Django 5.1 on 2024-08-31 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bazar", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="nome",
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
    ]
