# Generated by Django 5.1.4 on 2025-03-04 06:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
        ("company_report", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "createdDate",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="account.account",
                    ),
                ),
            ],
            options={
                "db_table": "orders",
            },
        ),
        migrations.CreateModel(
            name="OrdersItem",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "orders",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders_items",
                        to="orders.orders",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company_report.companyreport",
                    ),
                ),
            ],
            options={
                "db_table": "orders_item",
            },
        ),
    ]
