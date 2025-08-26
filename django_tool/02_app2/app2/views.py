from django.http import HttpResponse
from django.shortcuts import render
#def home(request):
#    return HttpResponse("Welcome to my Home page of AHN!")

def home(request):
    return render(request, 'app2/home.html')

def blogs(request):
    return render(request, 'blogs.html')



    return HttpResponse(html_content)

