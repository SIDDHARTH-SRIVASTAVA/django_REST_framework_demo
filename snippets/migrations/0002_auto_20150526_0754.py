# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='laguage',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='tite',
            new_name='title',
        ),
    ]
