# Generated by Django 4.1.3 on 2022-11-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_avartar_user_currency_user_gender_user_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avartar",
            field=models.URLField(blank=True),
        ),
    ]
