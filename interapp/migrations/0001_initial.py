# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 06:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('addr', models.URLField()),
                ('method', models.CharField(max_length=20)),
                ('enc', models.CharField(max_length=20)),
                ('inputs', models.CharField(db_column='input', max_length=2000)),
                ('output', models.CharField(max_length=20000)),
                ('createtime', models.DateTimeField(default=datetime.datetime(2016, 9, 27, 14, 55, 32, 921000))),
                ('result', models.BooleanField(default=False)),
                ('spend', models.FloatField()),
            ],
            options={
                'db_table': 'inter',
            },
        ),
    ]
