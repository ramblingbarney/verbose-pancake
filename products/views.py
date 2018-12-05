from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import NewProductForm, ProductAreaForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


@login_required
def new_product(request):
    new_product_form = NewProductForm()
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Feature/Issue created')
        else:
            messages.add_message(
                request, messages.ERROR, form.errors)

    args = {'new_product_form': new_product_form}
    return render(request, 'new_product.html', args)


def product_area(request):
    product_area_form = ProductAreaForm()
    if request.method == 'POST':
        form = ProductAreaForm(request.POST)
        if form.is_valid():
            # file is saved
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Product Area created')
        else:
            messages.add_message(
                request, messages.ERROR, form.errors)

    args = {'product_area_form': product_area_form}
    return render(request, 'product_area.html', args)
