# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]