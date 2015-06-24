from django.contrib import admin
from questions.models import Question, Comment, Tag, Person

admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Tag)

# Register your models here.
