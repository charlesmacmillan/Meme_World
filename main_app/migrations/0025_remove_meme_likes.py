# Generated by Django 3.0.8 on 2020-09-23 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_auto_20200923_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='likes',
        ),
    ]
