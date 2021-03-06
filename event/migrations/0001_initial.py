# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0006_auto_20161226_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='分类')),
                ('ename', models.CharField(max_length=50, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='城市')),
                ('encity', models.CharField(max_length=50, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='活动名称')),
                ('ename', models.CharField(max_length=50, verbose_name='Event Name')),
                ('hosts', models.CharField(max_length=254, verbose_name='主办')),
                ('organizer', models.CharField(max_length=254, verbose_name='承办')),
                ('contact', models.CharField(max_length=50, verbose_name='联系人')),
                ('address', models.CharField(max_length=254, verbose_name='联系地址')),
                ('phone', models.CharField(max_length=50, verbose_name='电话')),
                ('email', models.EmailField(max_length=254, verbose_name='电子邮件')),
                ('website', models.URLField(verbose_name='网址')),
                ('venue', models.CharField(max_length=254, verbose_name='场馆')),
                ('vaddress', models.CharField(max_length=254, verbose_name='地址')),
                ('start_at', models.DateTimeField(verbose_name='开始时间')),
                ('end_at', models.DateTimeField(verbose_name='结束时间')),
                ('intro', models.TextField(verbose_name='简介')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('verfied', models.BooleanField(default=False, verbose_name='审核状态')),
                ('image', models.ImageField(upload_to='', verbose_name='活动海报')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User')),
            ],
        ),
    ]
