# Generated by Django 5.1.4 on 2025-03-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="age_range",
            field=models.CharField(max_length=32),
        ),
    ]
