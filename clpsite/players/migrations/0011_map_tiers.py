# Generated by Django 3.2.6 on 2021-12-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_alter_player_agents'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='tierS',
            field=models.ManyToManyField(blank=True, help_text='Enter a tier S agent', to='players.Agent'),
        ),
    ]
