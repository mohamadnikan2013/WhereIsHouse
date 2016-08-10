# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160801_0530'),
        ('House', '0014_comment_is_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='member_like',
            field=models.ManyToManyField(to='account.Member', null=True),
        ),
    ]
