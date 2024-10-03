from django.shortcuts import render, redirect
from .models import Product, Category, Customer
from .forms import ProductForm, CategoryForm, CustomerForm, SearchForm

def home(request):
    return render(request, 'mi_app/home.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'mi_app/add_product.html', {'form': form})

def search_product(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)
            return render(request, 'mi_app/search_results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'mi_app/search.html', {'form': form})

