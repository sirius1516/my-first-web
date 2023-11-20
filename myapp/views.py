from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    items = ['iphone' 'android', 'samsung']
    return HttpResponse(items)

def contacts(request):
    return HttpResponse('<h1>Contacts</h1>')