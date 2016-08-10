# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0012_auto_20160802_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='replies',
        ),
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(blank=True, null=True, related_name='replies_rel_+', to='House.Comment'),
        ),
    ]
