# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0005_auto_20160801_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to='House_picture', blank=True, default='House_picture/HOuse.jpg/', null=True),
        ),
    ]
