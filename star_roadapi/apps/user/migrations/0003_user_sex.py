# Generated by Django 2.0.7 on 2020-08-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default='女生', max_length=12, verbose_name='性别'),
        ),
    ]
