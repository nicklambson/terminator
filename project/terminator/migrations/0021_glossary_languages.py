# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terminator', '0020_remove_summarymessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossary',
            name='other_languages',
            field=models.ManyToManyField(blank=True, related_name='_glossary_other_languages_+', to='terminator.Language', verbose_name='other languages'),
        ),
        # Just to add (disable) the related_name
        migrations.AlterField(
            model_name='glossary',
            name='source_language',
            field=models.ForeignKey(default=b'en', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='terminator.Language', verbose_name='source language'),
        ),
    ]
