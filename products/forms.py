import random
from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={
        'name': 'name',
        'type': 'text',
        'placeholder': 'Enter Product Name',
    }))

    productCode = print (random.randint(1,1000000001)*5)   
    
    code = forms.CharField(label=" Product Code", widget=forms.TextInput(attrs={
        'name': 'code',
        'type': 'text',
        'readonly': 'True',
        'value':   print(productCode),
    }))

    status = forms.CharField(label=" Product Status", widget=forms.TextInput(attrs={
        'name': 'status',
        'type': 'text',
        'readonly': 'True',
        'value':    'Available',
    }))
    
    class Meta:
        model = Products 
        fields = ['name', 'description', 'code', 'status']