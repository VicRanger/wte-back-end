# Generated by Django 2.0.5 on 2018-06-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wte', '0002_auto_20180604_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='canteen',
            name='pos',
            field=models.CharField(default='shahe', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='up_users',
            field=models.ManyToManyField(blank=True, related_name='up_users', to='wte.User'),
        ),
    ]
