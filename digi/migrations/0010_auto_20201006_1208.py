# Generated by Django 2.2.10 on 2020-10-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0009_auto_20201006_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
