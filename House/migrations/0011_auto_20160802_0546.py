# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0010_auto_20160802_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ForeignKey(default=0, to='House.Comment', related_name='root_reply'),
            preserve_default=False,
        ),
    ]
