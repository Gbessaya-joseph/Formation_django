from django.shortcuts import render
from .models import Product
from .form import ProductForm, RowProductForm
from django.http import HttpResponse

# Create your views here.


def product_list(request, *args, **kwargs):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'list.html', context)


def product_create(request):
    messages = ""
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "Product created successfully"
    return render(request, 'create.html', {'form': form, 'message': messages})

#request.FILES après request.POST