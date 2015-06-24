import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ask_boldyrev.settings')

import django
django.setup()

from questions.models import Question, Comment, Tag, Person
