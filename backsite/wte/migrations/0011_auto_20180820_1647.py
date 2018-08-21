# Generated by Django 2.0.5 on 2018-08-20 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wte', '0010_canteen_vis_cnt'),
    ]

    operations = [
        migrations.AddField(
            model_name='canteen',
            name='timetable',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='item',
            name='canteen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wte.Canteen'),
        ),
    ]