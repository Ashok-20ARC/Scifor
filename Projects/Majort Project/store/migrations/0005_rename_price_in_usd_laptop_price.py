# Generated by Django 5.1.7 on 2025-03-17 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_price_laptop_price_in_usd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='price_in_usd',
            new_name='price',
        ),
    ]
