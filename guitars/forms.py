from django import forms 

from .models import Client, Product, Sale

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }

class SaleForm(forms.ModelForm):                                          
    class Meta:                                                             
        model = Sale                                                      
        fields = '__all__'                                                  
        widgets = {                                                         
            'client': forms.Select(attrs={'class': 'form-control'}),     
            'product': forms.Select(attrs={'class': 'form-control'}),       
	    'total': forms.TextInput(attrs={'class': 'form-control'}),      
 	    'date': forms.TextInput(attrs={'class': 'form-control'})     
        }                                                                   
          
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_selling': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'})
        }
#Para agregar stock si un producto ya existe :p
class ProductStockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku', 'stock']  
