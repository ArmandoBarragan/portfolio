from django.shortcuts import render, redirect
from store.models import Category, Product
from store.forms import CategoryForm, ProductForm
from store import utils
# Create your views here.
def edit_view(request, id):
    product = Product.objects.get(pk=id)
    context = {
        'product': product,
        'product_form': ProductForm(),
        'title': 'Edit product',
    }
    return render(request, 'store/edit_product.html', context=context)


def delete(request, id):
    product = Product.objects.filter(id=id)
    product.delete()
    return redirect('store')


def home(request):
    products = Product.objects.all()
    if request.method == 'GET' and request.GET.get('busqueda') != None:
        query = request.GET.get('busqueda')
        products = Product.objects.filter(name__contains=query)

    product_form = ProductForm()
    category_form = CategoryForm()

    context = {
        "products": products,
        "category_form": category_form,
        "product_form": product_form,
        'title': 'Store',
    }
    return render(request, 'store/store.html', context=context)


def post_category(request):
    if request.method == 'POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            utils.save_category(category)
    return redirect('store')

        
def post_product(request):
    if request.method == 'POST':
        product = ProductForm(request.POST, request.FILES)
        if product.is_valid():
            product.save()
    return redirect('store')


def update(request, pk):
    product = Product.objects.get(pk=pk)
    product_form = ProductForm(request.POST, request.FILES)

    if product_form.is_valid():
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        else:
            product.image = '../media/broken.png'
        
        utils.replace_product_attributes(product, product_form)
        product_form.save()

    return redirect('store')
