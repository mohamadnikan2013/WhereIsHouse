# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('profile_picture', models.ImageField(null=True, blank=True, upload_to='profile_pictures/')),
                ('is_verified', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=100)),
                ('primary_user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='member')),
            ],
        ),
    ]
