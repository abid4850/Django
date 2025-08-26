from django.http import HttpResponse
from django.shortcuts import render
#def home(request):
#    return HttpResponse("Welcome to my Home page of AHN!")

def home(request):
    # Render the index page from the app's templates so the root URL shows index.html
    return render(request, 'app2/index.html')

def blogs(request):
    # Use a template for blogs so styling is consistent
    return render(request, 'app2/blogs.html')

