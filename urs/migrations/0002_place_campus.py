# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='campus',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
