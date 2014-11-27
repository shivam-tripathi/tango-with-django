# Commented out because of being there in the default config but not being
# used.
from django.shortcuts import render

# django.template import render
from django.http import HttpResponse

# Index page 
def index(request):
	context_dict = {'boldmessage':'I am bold from the context'}
	return render(request, 'rango/index.html', context_dict)

# About page
def about(request):
	return HttpResponse("Hello E-410")