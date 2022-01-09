from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def quote(request):
    return HttpResponse("<h1>Here we go</h1>")
