from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import RequestContext, loader
from questions.models import *
from django.contrib.auth import authenticate, login, logout
import re

def question_list(request):
	vardict = check_login(request)
	vardict.update( check_sort_and_paginator(request, Question.objects.all()) )
	vardict.update( right_block() )
	return render(request, 'questions/question_list.html', vardict)

def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	page = 1
	if(request.method == "POST"):
		if("goto_page" in request.POST.keys()):
			try:
				page = int( request.POST["goto_page"] )
			except:
				page = 1
		if("new_comment_text" in request.POST.keys() and len(request.POST["new_comment_text"]) > 0):
			from django.utils import timezone
			new_comment = Comment(
				question = question,
				author = request.user,
				comment_text=request.POST["new_comment_text"],
				pub_date = timezone.now(),
				is_right = False
				)
			new_comment.save()
	vardict =  { 
		'question': question,
		'comments': question.comment_set.order_by('-pub_date').order_by('-rating')[ 30*(page-1) : 30*page ],
		'page_list': range(1, int( question.comment_set.count() - 1 ) / 30 + 2 ),
		'page': page,
	}
	if( page > 1 ): vardict.update( { 'prev_page': (page-1) } )
	if( 30*page < question.comment_set.count() ): vardict.update( { 'next_page': (page+1) } )
	vardict.update( check_login(request) )
	vardict.update( right_block() )
	return render(request, 'questions/question.html', vardict)

def tag(request, tag_text):
	vardict = check_login(request)
	vardict.update( right_block() )
	try:
		tag = Tag.objects.get(tag_text=tag_text)
		questions = tag.questions.order_by('-pub_date')
		vardict.update( check_sort_and_paginator(request, questions) )
		vardict.update( {
			'status_message': 'Questions by tag: ' + tag_text,
			'tag': tag,
		} )
		return render(request, 'questions/question_list.html', vardict)
	except:
		vardict.update( {
			'status_message': 'No such tag (' + tag_text + ') !',
		} )
		return render(request, 'questions/question_list.html', vardict)
		

def new_question(request):
	if( not request.user.is_authenticated() ):
		return render(request, 'redirect.html', {'redirect_url': "/questions/question_list"} )
	if(request.method == "POST"):
		if("new_question_title" in request.POST.keys() and 
			"new_question_text" in request.POST.keys() and
			len(request.POST["new_question_title"]) > 0 and
			len(request.POST["new_question_text"]) > 0 ):
				from django.utils import timezone
				new_question = Question(
					question_title = request.POST["new_question_title"],
					question_text = request.POST["new_question_text"],
					author = request.user,
					pub_date = timezone.now()
					)
				new_question.save()
				for new_quest_tag in [ t.replace(',','') for t in request.POST['new_question_tags'].split(' ') ]:
					if( len(new_quest_tag) == 0 ): continue
					try:
						tag = Tag.objects.get(tag_text = new_quest_tag)
					except:
						tag = Tag(tag_text = new_quest_tag)
					tag.save()
					tag.questions.add( new_question )
					tag.save()
				new_question.save()
				return render(request, 'redirect.html', {'redirect_url': "/questions/question_list"} )
	vardict = check_login(request)
	vardict.update( right_block() )
	return render(request, 'questions/new_question.html', vardict)

def profile(request):
	vardict = check_login(request)
	vardict.update( right_block() )
	return render(request, 'questions/profile.html', vardict)

def register(request):
	if( request.user.is_authenticated() ):
		return render(request, 'redirect.html', {'redirect_url': "/questions/question_list"} )
	vardict = check_login(request)
	vardict.update( right_block() )
	return render(request, 'questions/register.html', vardict)


def right_block():
	return {
		'popular_tags': Tag.objects.order_by('-absolute_popularity')[:50],
		'best_members': [p.user.username for p in Person.objects.order_by('-rating')[:5] ],
	}

def check_login(request):
	"""
	Check for POST params to query
	login functions
	Returns an update for vardict
	"""
	login_msg = ""
	if(request.method == "POST"):
		if("login" in request.POST.keys() and "password" in request.POST.keys()):
			user = authenticate(username = request.POST["login"], password = request.POST["password"])
			if(user is not None):
				if(user.is_active):
					login(request, user)
				else:
					login_msg = "user is inactive"
			else:
					login_msg = "invalid credentials"
		if("log_out" in request.POST.keys() and request.user.is_authenticated()):
			logout(request)
	return {
		'login_msg': login_msg,
	}



def check_sort_and_paginator(request, questions):
	"""
	Check for POST params to query
	question list sort functions
	and pages
	Returns an update for vardict
	"""
	offset = 0
	sort_param = 'pub_date'
	sort_direction = 'downwards'
	question_count = questions.count()
	if(request.method == "POST"):
		if("offset" in request.POST.keys()):
			try:
				offset = int( request.POST["offset"] )
			except:
				offset = 0
		if("sort_param" in request.POST.keys()):
			sort_param = request.POST["sort_param"]
		if("sort_direction" in request.POST.keys()):
			sort_direction = request.POST["sort_direction"]
		for key in request.POST.keys():
			if key[:7] == "rating.":
				if not request.user.is_authenticated(): break
				r = re.search("rating\.([0-9]*)\.(.*)", key).groups()
				if r is None or len(r) != 2: break
				( question_id, updown ) = r
				question_to_rate = Question.objects.get(pk=question_id)
				import pdb
				pdb.set_trace()
				if question_to_rate is None: break
				if updown == 'up' and question_to_rate.can_like(request.user):
					if(request.user in question_to_rate.users_disliked):
						question_to_rate.users_disliked.remove(request.user)
					else:
						question_to_rate.users_liked.add(request.user)
						question_to_rate.save() 
				if updown == 'down' and question_to_rate.can_dislike(request.user):
					if(request.user in question_to_rate.users_liked):
						question_to_rate.users_liked.remove(request.user)
					else:
						question_to_rate.users_disliked.add(request.user)
						question_to_rate.save() 
	if(sort_param == "rating"):
		if(sort_direction == "upwards"):
			questions = questions.order_by('rating')
		else:
			questions = questions.order_by('-rating')
	else:	
		if(sort_direction == "upwards"):
			questions = questions.order_by('pub_date')
		else:
			questions = questions.order_by('-pub_date')
	questions = questions[offset:offset+20]
	page = int( offset / question_count ) + 1
	pages_count = int( question_count / 20 ) + 1
	if( offset == 0 ):
		prev_page_offset = -1
	else:
		prev_page_offset = offset - 20
		if( prev_page_offset < 0 ): prev_page_offset = 0
	if( offset + 20 < question_count ):
		next_page_offset = offset + 20
	else:
		next_page_offset = -1
	page_list = [0, ]
	page_list.append( offset % 20 )
	n = 1
	while( n * 20 + page_list[1] <= question_count ):
		page_list.append( n * 20 + page_list[1] )
		n = n + 1
	if( page_list[0] == page_list[1] ):
		page_list = page_list[1:]
	return( {
        'questions': questions,
		'sort_param': sort_param,
		'sort_direction': sort_direction,
		'page': page,
		'pages_count': pages_count,
		'offset': offset,
		'prev_page_offset': prev_page_offset,
		'next_page_offset': next_page_offset,
		'page_list': page_list,
	} )
