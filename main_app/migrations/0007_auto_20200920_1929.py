# Generated by Django 3.1.1 on 2020-09-20 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200920_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='created_on',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
