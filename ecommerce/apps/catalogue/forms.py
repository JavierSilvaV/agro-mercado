from django import forms

from .models import Category, Product, ProductImage


class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'regular_price', 'discount_price', 'stock', 'category', 'product_type', 'is_active', 'vendedor', 'slug']

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class imageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text', 'is_feature']
