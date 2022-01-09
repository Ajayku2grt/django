from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def display(request):
    return HttpResponse("<h1>Here, my new djnago project</h1><br><p> Shifting to new technology, actually which I was previous;y using</p>")

def displaydatetime(request):
    dt=datetime.datetime.now()
    s="<p>Current time now is</p>"+str(dt)
    return HttpResponse(s)
