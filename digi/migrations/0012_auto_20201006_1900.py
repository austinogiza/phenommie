# Generated by Django 2.2.10 on 2020-10-06 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0011_auto_20201006_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='icon',
            new_name='image',
        ),
    ]
