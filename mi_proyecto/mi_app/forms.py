from django import forms
from .models import Product, Category, Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
