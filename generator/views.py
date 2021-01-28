from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')
      
def about(request):
    return render(request, 'generator/about.html')
    
def password(request):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    
    if(request.GET.get('uppercase')):
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if(request.GET.get('special')):
        characters += '!@$%^&()'
    if(request.GET.get('numbers')):
        characters += '123456789'
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator\password.html', {'password':thepassword})
