from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, "myapp/index.html", context)


def index_item(request, my_id):
    return HttpResponse('Your item id is: ' + str(my_id))

def contacts(request):
    return render(request, 'myapp/contacts.html')