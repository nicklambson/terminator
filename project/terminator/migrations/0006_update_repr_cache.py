# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 18:28
from __future__ import unicode_literals

from django.db import migrations


def create_concept_reprs(apps, schema_editor):
    # This is a bit slow, but should not affect many people.
    Concept = apps.get_model('terminator', 'Concept')
    for c in Concept.objects.filter(repr_cache__isnull=True):
        src_translations = c.translation_set.filter(
                language_id=c.glossary.source_language_id,
        )
        repr_ = ', '.join(t.translation_text for t in src_translations)
        if repr_:
            c.repr_cache = "#%d: %s" % (c.id, repr_)
        c.save(update_fields=['repr_cache'])


class Migration(migrations.Migration):

    dependencies = [
        ('terminator', '0005_add_concept_repr_cache'),
    ]

    operations = [
        migrations.RunPython(create_concept_reprs, migrations.RunPython.noop)
    ]
