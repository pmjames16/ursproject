# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urs', '0005_place_camp'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='img',
            field=models.CharField(default='./../static/img/background2.jpg', max_length=200),
        ),
        migrations.AddField(
            model_name='place',
            name='usage',
            field=models.CharField(default='행사', max_length=200),
        ),
    ]
