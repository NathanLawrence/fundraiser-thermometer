from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<p>Index View</p>')

def fetchsquare(request, id):
	return HttpResponse('<p>Square fetch of {0}</p>'.format(id))

