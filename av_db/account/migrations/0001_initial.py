# Generated by Django 5.1.4 on 2025-03-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.CharField(max_length=32)),
                ("gender", models.CharField(default="Unknown", max_length=32)),
                ("birthyear", models.IntegerField(default="Unknown")),
                ("age_range", models.CharField(max_length=32, unique=True)),
            ],
            options={
                "db_table": "account",
            },
        ),
        migrations.CreateModel(
            name="AccountRoleType",
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
                    "roleType",
                    models.CharField(
                        choices=[("ADMIN", "Admin"), ("NORMAL", "Normal")],
                        default="NORMAL",
                        max_length=64,
                    ),
                ),
            ],
            options={
                "db_table": "account_role_type",
            },
        ),
    ]
