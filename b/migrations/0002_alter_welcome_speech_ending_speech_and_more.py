# Generated by Django 4.1.4 on 2022-12-28 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcome_speech',
            name='Ending_speech',
            field=models.TextField(verbose_name='ENDING SPEECH'),
        ),
        migrations.AlterField(
            model_name='welcome_speech',
            name='welcome_speech',
            field=models.TextField(verbose_name='WELCOME SPEECH'),
        ),
    ]
