from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse( "<html><body><h1>Practice Project</h1></body></html>")
