# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pictures/', default='profile_pictures/funny-profile-pictures.jpg/'),
        ),
    ]
