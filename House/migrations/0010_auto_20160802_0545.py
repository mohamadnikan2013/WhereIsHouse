# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0009_auto_20160802_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(default=0, related_name='replies', to='House.Comment'),
            preserve_default=False,
        ),
    ]
