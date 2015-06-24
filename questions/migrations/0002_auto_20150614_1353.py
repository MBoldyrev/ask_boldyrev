# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='dislikes_number',
        ),
        migrations.RemoveField(
            model_name='question',
            name='likes_number',
        ),
    ]
