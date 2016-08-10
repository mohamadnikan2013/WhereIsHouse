# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0013_auto_20160803_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_reply',
            field=models.BooleanField(default=False),
        ),
    ]
