from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# Create your views here.
def course_list(request):
	courselist=Course.objects.all()
	return HttpResponse(courselist)