from django.shortcuts import render

# Create your views here.
def home_page_view(request):
	return render(request, 'website/base.html')

def python_page_view(request):
	return render(request, 'website/python.html')

def django_page_view(request):
	return render(request, 'website/django.html')

def web_dev_page_view(request):
	return render(request, 'website/web_dev.html')
