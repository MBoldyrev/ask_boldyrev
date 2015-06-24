# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='comments_number',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
        ),
    ]
