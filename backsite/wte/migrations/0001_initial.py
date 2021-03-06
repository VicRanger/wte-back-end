# Generated by Django 2.0.5 on 2018-06-04 12:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canteen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ename', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200)),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create-time')),
                ('mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last-mod-time')),
                ('up', models.IntegerField(default=0)),
                ('canteen', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wte.Canteen')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ename', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=200)),
                ('avatar_url', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wte.Item'),
        ),
        migrations.AddField(
            model_name='comment',
            name='up_users',
            field=models.ManyToManyField(blank=True, related_name='up_users', to='wte.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wte.User'),
        ),
    ]
