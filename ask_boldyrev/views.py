from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render_to_response
import cgi, os, ask_boldyrev

@csrf_exempt 
def show_request_params(request):
	html = "<html><body>Hello, world!<br>\n"
	# html += str(request) + "\n"
	if request.method == 'GET':
		html += "GET parameters: <br>\n"
		for k in request.GET.keys():
			html += str(k) + " : " + request.GET[k] + "<br>\n"
	elif request.method == 'POST':
		html += "POST parameters: <br>\n"
		# parameters = cgi.parse_qs(request.META['QUERY_STRING'])
		for k in request.POST.keys():
			html += str(k) + " : " + str(request.POST[k][0]) + "<br>\n"
	html += "</body></html>" 
	return HttpResponse(html)


def main(request):
	return render_to_response("main.html")

