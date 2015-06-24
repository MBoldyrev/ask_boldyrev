# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_question_correct_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_comment',
            field=models.ForeignKey(related_name='correct_comment', to='questions.Comment', null=True),
        ),
    ]
