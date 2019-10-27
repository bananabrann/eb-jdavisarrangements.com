from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Hello from Home!')

def about(request):
    return HttpResponse('Hello there from About!')