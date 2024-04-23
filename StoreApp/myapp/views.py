from django.shortcuts import render
from .models import Product
from django.http import Http404

def show(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'myapp/show.html', {'product': product})
