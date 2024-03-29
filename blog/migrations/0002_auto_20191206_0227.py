# Generated by Django 2.2.7 on 2019-12-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='sushi',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='direccion',
            field=models.CharField(default='', max_length=220),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='nombre',
            field=models.CharField(default='', max_length=180),
            preserve_default=False,
        ),
    ]
