# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20150618_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
