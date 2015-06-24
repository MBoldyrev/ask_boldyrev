# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20150619_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='rating',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
        ),
    ]
