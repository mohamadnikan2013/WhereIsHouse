# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to='/House/static/House/image', null=True, blank=True),
        ),
    ]
