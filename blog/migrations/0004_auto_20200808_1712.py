# Generated by Django 3.0.8 on 2020-08-08 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200808_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='comment',
            new_name='content',
        ),
    ]
