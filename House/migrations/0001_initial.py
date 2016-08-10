# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('site', models.CharField(null=True, max_length=10)),
                ('response_time', models.CharField(null=True, max_length=25)),
                ('phone', models.CharField(null=True, max_length=20)),
                ('email', models.CharField(null=True, max_length=50)),
                ('token', models.CharField(unique=True, max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('price1', models.IntegerField(null=True, blank=True)),
                ('price2', models.IntegerField(null=True, blank=True)),
                ('time', models.DateTimeField(auto_now=True, max_length=50)),
                ('image_url', models.CharField(null=True, max_length=100)),
                ('description', models.CharField(null=True, max_length=500)),
                ('square', models.IntegerField(null=True)),
                ('room_num', models.IntegerField(null=True)),
                ('region', models.CharField(null=True, max_length=50)),
                ('city', models.CharField(null=True, max_length=50)),
                ('image', models.ImageField(null=True, upload_to='House/static/House/image')),
                ('user', models.ForeignKey(to='account.Member', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='house',
            field=models.ForeignKey(to='House.Home', related_name='comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='member',
            field=models.ForeignKey(to='account.Member', related_name='comment'),
        ),
    ]
