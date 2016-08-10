# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0011_auto_20160802_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replies',
            field=models.ForeignKey(null=True, blank=True, to='House.Comment', related_name='root_reply'),
        ),
    ]
