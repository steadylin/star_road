# Generated by Django 2.0.7 on 2020-08-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signature',
            field=models.CharField(default='分享美好生活', help_text='最大长度200', max_length=200),
        ),
    ]
