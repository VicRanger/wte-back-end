# Generated by Django 2.0.5 on 2018-08-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wte', '0009_auto_20180713_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='canteen',
            name='vis_cnt',
            field=models.IntegerField(default=0),
        ),
    ]