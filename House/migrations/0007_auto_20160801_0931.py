# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160801_0530'),
        ('House', '0006_auto_20160801_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='user',
        ),
        migrations.AddField(
            model_name='home',
            name='member',
            field=models.ForeignKey(related_name='houses', to='account.Member', null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(default='House_picture/House.jpeg/', null=True, blank=True, upload_to='House_picture/'),
        ),
    ]
