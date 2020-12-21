from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# use HOME function using 'request' arg.
def home(request):
	return HttpResponse('<h1>Blog Home</h1>')


def about(request):
	return HttpResponse('<h1>Blog About</h1>')