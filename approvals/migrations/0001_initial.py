# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 03:10
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approvalstate', models.IntegerField(choices=[(0, 'Requested'), (1, 'Assigned'), (2, 'Approved'), (3, 'Declined')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('approvaldata', annoying.fields.JSONField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('approval_at', models.DateTimeField(blank=True, null=True)),
                ('approval_reason', models.CharField(blank=True, max_length=50)),
                ('approval_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approver', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'approval',
                'verbose_name_plural': 'approvals',
            },
        ),
    ]