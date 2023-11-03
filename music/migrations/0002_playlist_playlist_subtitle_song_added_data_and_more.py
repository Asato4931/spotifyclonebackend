# Generated by Django 4.2.5 on 2023-11-03 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='playlist_subtitle',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='song',
            name='added_data',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='song',
            name='album_title',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.CharField(default='', max_length=250),
        ),
    ]
