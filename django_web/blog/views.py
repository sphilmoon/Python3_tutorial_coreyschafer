# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# use HOME function using 'request' arg.
def home(request):
	context = {
		'people': people
	}
	return render(request, 'blog_temp/home.html', context)

def about(request):
	return render(request, 'blog_temp/about.html', {'title': 'About'})

# dummy data.
people = {'Name': 'Ford Prefect',
'Gender': 'Male',
'Occupation': 'Researcher', 
'Home_Planet': 'Betelgeuse Seven' },
{'Gender': 'Female', 
'Occupation': 'Mathematician', 
'Home Planet': 'Earth' },
{'Occupation': 'Sandwich-Maker', 
'Gender': 'Male', 'Home Planet': 'Earth', 
'Name': 'Arthur'}


# def about(request):
#	return HttpResponse('<h1>Blog About</h1>')