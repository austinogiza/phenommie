# Generated by Django 3.0.7 on 2020-08-24 13:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_remove_userlibrary_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
