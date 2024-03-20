from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'image', 'slug',)


class RowProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    slug = forms.SlugField()
