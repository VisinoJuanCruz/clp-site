# Generated by Django 3.2.6 on 2021-11-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_player_agents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='agents',
            field=models.ManyToManyField(blank=True, help_text='Enter a agents', to='players.Agent'),
        ),
    ]
