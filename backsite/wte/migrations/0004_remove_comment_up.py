# Generated by Django 2.0.5 on 2018-06-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wte', '0003_auto_20180608_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='up',
        ),
    ]
