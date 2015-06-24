# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_question_comments_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_comment',
            field=models.ForeignKey(related_name='correct_comment', default='', to='questions.Comment', null=True),
            preserve_default=False,
        ),
    ]
