# Generated by Django 2.0.7 on 2020-08-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0002_auto_20200809_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='display_order',
            field=models.IntegerField(verbose_name='排序'),
        ),
    ]
