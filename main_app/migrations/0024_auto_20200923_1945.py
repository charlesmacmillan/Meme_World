# Generated by Django 3.0.8 on 2020-09-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_meme_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
