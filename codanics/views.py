from django.http import HttpResponse
from django.shortcuts import render

# Create home view
def home(request):
    return HttpResponse("Welcome to the Home Page Abid!")

# Create blog view
#def blog(request):
#    return HttpResponse("Welcome to the Blog Page")
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')
