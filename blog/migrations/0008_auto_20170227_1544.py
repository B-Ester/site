# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170227_1425'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comments',
            table='comments',
        ),
    ]
