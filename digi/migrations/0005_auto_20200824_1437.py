# Generated by Django 3.0.7 on 2020-08-24 13:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0004_auto_20200819_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='end_body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='content_body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]