# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20161227_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='活动海报'),
        ),
    ]
