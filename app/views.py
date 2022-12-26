from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('first programe')
def lavanya(request):
    return HttpResponse('<h1><marquee>lavanya</marquee></h1>')