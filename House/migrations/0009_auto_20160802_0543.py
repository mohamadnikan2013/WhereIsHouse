# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0008_comment_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ManyToManyField(to='House.Comment', related_name='replies'),
        ),
    ]
