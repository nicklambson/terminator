# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminator', '0008_less_required_fields'),
    ]

    operations = [
            migrations.RenameField("Proposal",
                old_name="word",
                new_name="term",
            ),
        migrations.AlterField(
            model_name='proposal',
            name='term',
            field=models.CharField(max_length=100, verbose_name='term'),
        ),

    ]
