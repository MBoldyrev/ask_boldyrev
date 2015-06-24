# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_auto_20150614_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes_number',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes_number',
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2),
        ),
        migrations.AddField(
            model_name='comment',
            name='users_disliked',
            field=models.ManyToManyField(related_name='comment_users_disliked', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='users_liked',
            field=models.ManyToManyField(related_name='comment_users_liked', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_right',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='users_disliked',
            field=models.ManyToManyField(related_name='question_users_disliked', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='users_liked',
            field=models.ManyToManyField(related_name='question_users_liked', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
