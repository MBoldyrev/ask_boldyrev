# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('likes_number', models.DecimalField(default=0, max_digits=3, decimal_places=0)),
                ('dislikes_number', models.DecimalField(default=0, max_digits=3, decimal_places=0)),
                ('is_right', models.NullBooleanField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('likes_number', models.DecimalField(default=0, max_digits=3, decimal_places=0)),
                ('dislikes_number', models.DecimalField(default=0, max_digits=3, decimal_places=0)),
                ('rating', models.DecimalField(default=0, max_digits=3, decimal_places=2)),
                ('author', models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL)),
                ('users_disliked', models.ManyToManyField(related_name='users_disliked', to=settings.AUTH_USER_MODEL, blank=True)),
                ('users_liked', models.ManyToManyField(related_name='users_liked', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_text', models.CharField(max_length=200)),
                ('absolute_popularity', models.DecimalField(default=0, max_digits=3, decimal_places=0)),
                ('questions', models.ManyToManyField(to='questions.Question')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(to='questions.Question'),
        ),
    ]
