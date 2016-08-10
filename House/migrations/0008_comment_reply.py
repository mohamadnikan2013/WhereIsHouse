# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160801_0530'),
        ('House', '0007_auto_20160801_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(default=0, to='account.Member', related_name='reply'),
            preserve_default=False,
        ),
    ]
