from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewProductForm, ProductAreaForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.models import F


@csrf_protect
def all_products(request):
    if request.is_ajax() and request.method == 'POST':
        Product.objects.filter(
            id=request.POST['vote_id']).update(votes=F('votes') + 1)
        return HttpResponse(request.POST['vote_id'])
    else:
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
            return redirect('products')
        else:
            messages.add_message(
                request, messages.ERROR, form.errors)

    args = {'new_product_form': new_product_form}
    return render(request, 'new_product.html', args)


@login_required
def edit_product(request, id=None, template_name='edit_product.html'):
    if id:
        product = get_object_or_404(Product, id=id)

    new_product_form = NewProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product,
        id=id)

    if request.POST and new_product_form.has_changed():

        if new_product_form.is_valid():
            product.save()
            return redirect('products')

    elif request.POST:
        messages.add_message(
            request, messages.ERROR, 'No changes to save')

    args = {'new_product_form': new_product_form, 'id': id}
    return render(request, template_name, args)


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
