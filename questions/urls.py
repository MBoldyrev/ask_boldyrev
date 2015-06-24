from django.conf.urls import patterns, include, url
from questions import views

urlpatterns = patterns('',
	url(r'^question_list', views.question_list, name='question_list'),
	url(r'^question/(?P<question_id>\d+)$', views.question, name='question'),
	url(r'^tag/(?P<tag_text>\w+)$', views.tag, name='tag'),
	url(r'^question/new$', views.new_question, name='new_question'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^register/$', views.register, name='register'),

)
