# Generated by Django 3.2.6 on 2021-12-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0015_auto_20211203_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='map',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='map',
            name='minimapa',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
