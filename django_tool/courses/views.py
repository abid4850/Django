from django.shortcuts import render, get_object_or_404
from courses.models import Courses
from django.http import HttpResponse


# Create your views here.
def course_detail(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    # print(course)
    # return HttpResponse(course)
    context = {
        'course': course,
    }
    return render(request, 'course_detail.html', context)


generative ai, agentic ai, llms, RAG AND CAG , DATA SCRAPING, nlp, fine tuning llms prompt engineering, ai agents and n8n, django mvt