# Generated by Django 3.0.7 on 2020-10-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0015_auto_20201006_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='header',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='services',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
