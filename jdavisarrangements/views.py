from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hello from Home!')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('Hello there from About!')
    return render(request, 'about.html')