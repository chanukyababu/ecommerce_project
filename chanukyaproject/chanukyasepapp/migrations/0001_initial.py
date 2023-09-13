# Generated by Django 4.2.5 on 2023-09-05 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
                ("is_resolved", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Useradd",
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
                ("username", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
