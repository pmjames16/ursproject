# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urs', '0004_remove_place_campus'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='camp',
            field=models.CharField(max_length=200, default='bonwon'),
        ),
    ]
