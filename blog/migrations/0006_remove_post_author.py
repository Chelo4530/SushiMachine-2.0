# Generated by Django 2.2.7 on 2019-12-06 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]