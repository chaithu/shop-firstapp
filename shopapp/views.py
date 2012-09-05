from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

def home(request):
	return render_to_response("base.html")
def userpage(request):
	return HttpResponse(html)