# Generated by Django 3.0 on 2020-08-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
