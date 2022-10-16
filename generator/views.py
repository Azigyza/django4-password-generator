from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return  render(request,  'generator/home.html',  {'password' : 'Ghanaba12345Accra'})
def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty!!</h1>')
def password(request):

    characters = list('abcdefghijklmnopqrxtuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*+'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    length =  int(request.GET.get("length", 14)) # note 14 is default value
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render( request, 'generator/password.html',  {'password':thepassword})
def about(request):
    return render( request, 'generator/about.html')
