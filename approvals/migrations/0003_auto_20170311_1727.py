# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-11 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approvals', '0002_auto_20170222_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='approvaldata',
            field=models.TextField(blank=True),
        ),
    ]
