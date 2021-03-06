# Generated by Django 3.2.6 on 2021-11-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_player_agents_pool'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='name',
            field=models.CharField(help_text='Enter a name for this setup', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='setup',
            name='headset',
            field=models.CharField(help_text='Enter a headset name', max_length=50),
        ),
        migrations.AlterField(
            model_name='setup',
            name='keyboard',
            field=models.CharField(help_text='Enter a keyboard name', max_length=50),
        ),
        migrations.AlterField(
            model_name='setup',
            name='monitor',
            field=models.CharField(help_text='Enter a monitor name', max_length=50),
        ),
        migrations.AlterField(
            model_name='setup',
            name='mouse',
            field=models.CharField(help_text='Enter a mouse name', max_length=50),
        ),
        migrations.AlterField(
            model_name='setup',
            name='mousepad',
            field=models.CharField(help_text='Enter a mousepad name', max_length=50),
        ),
    ]
