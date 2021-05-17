from django import forms
from store.models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ['name', 'category', 'price', 'image']

    def save_attributes(self, product_form):
        data = product_form.cleaned_data
        self.name = data['name']
        self.category = data['category']
        self.price = data['price']
