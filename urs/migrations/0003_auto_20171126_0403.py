# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urs', '0002_place_campus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='campus',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
    ]
