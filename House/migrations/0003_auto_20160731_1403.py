# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0002_auto_20160731_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='media'),
        ),
    ]
