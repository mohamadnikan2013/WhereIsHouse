# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0004_auto_20160801_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, default='House_picture/funny-profile-pictures.jpg/', null=True, upload_to='House_picture'),
        ),
    ]
