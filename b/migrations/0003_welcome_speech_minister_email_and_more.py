# Generated by Django 4.1.4 on 2022-12-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0002_alter_welcome_speech_ending_speech_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcome_speech',
            name='minister_email',
            field=models.EmailField(default='admin@jesus.com', max_length=254),
        ),
        migrations.AddField(
            model_name='welcome_speech',
            name='minister_name',
            field=models.CharField(default='Pastor SAMUEL Ajayi', max_length=200),
        ),
    ]
