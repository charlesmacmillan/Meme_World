# Generated by Django 3.0.8 on 2020-09-23 21:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0030_remove_meme_users_who_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='likes',
        ),
        migrations.AddField(
            model_name='meme',
            name='likes',
            field=models.ManyToManyField(related_name='meme_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
