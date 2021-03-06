# Generated by Django 3.0.8 on 2020-09-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0032_auto_20200923_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meme',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='meme',
            name='font_size',
            field=models.CharField(blank=True, choices=[('15px', '10pt'), ('20px', '20pt'), ('25px', '25pt'), ('30px', '30pt')], default='20px', max_length=5),
        ),
    ]
