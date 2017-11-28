# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urs', '0003_auto_20171126_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='campus',
        ),
    ]
