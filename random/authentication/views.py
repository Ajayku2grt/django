from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Loginform
from .forms import FormloginForm
# Create your views here.

def home(request):
    data = Loginform.objects.all()
    return render(request, 'authentication/index.html',{'data' : data})

def homenew(request):
    return HttpResponse("<p>With new method  integration is successful</p>")

def signup(request):
    form = FormloginForm()
    if request.method == 'POST':
         form =FormloginForm(request.POST)
         if form.is_valid():
             username = FormloginForm.cleaned_data['username']
             form.save()
             request.session['username'] = username
             return redirect('/home')
    return render(request, 'authentication/signup.html',{'form': form })

def signin(request):
    return render(request, 'authentication/signin.html')

def logout(request):
    pass
