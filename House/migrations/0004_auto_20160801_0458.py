# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0003_auto_20160731_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='0(.*)')], null=True, max_length=20),
        ),
    ]
