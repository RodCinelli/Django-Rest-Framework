# Generated by Django 5.1.4 on 2025-01-21 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ["-id"]},
        ),
    ]
