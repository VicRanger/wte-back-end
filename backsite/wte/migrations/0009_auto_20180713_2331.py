# Generated by Django 2.0.6 on 2018-07-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wte', '0008_user_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='province',
            field=models.CharField(default='null', max_length=100),
        ),
    ]