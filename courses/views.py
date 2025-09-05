from django.shortcuts import render, get_object_or_404
from courses.models import Courses
from django.http import HttpResponse

# Create your views here.

def course_detail(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    #print(course)
    #return HttpResponse(f"Course {course.title}")
    return render(request, 'courses/course_detail.html', {'course': course})