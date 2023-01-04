# Generated by Django 4.1.5 on 2023-01-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_car"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="cars",
            field=models.ManyToManyField(
                to="users.car", verbose_name="los carros de la persona"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                max_length=30, verbose_name="el nombre de la persona"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                max_length=30, verbose_name="el apellido de la persona"
            ),
        ),
        migrations.AlterField(
            model_name="website", name="url", field=models.URLField(unique=True),
        ),
    ]
