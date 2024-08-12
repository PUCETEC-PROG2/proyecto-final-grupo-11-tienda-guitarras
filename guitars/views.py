from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Client, Product
from guitars.forms import ClientForm, ProductForm, ProductStockForm


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

#Login
class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    
#Vista para desplegar los clientes

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients':clients})

    
@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('guitars:index')
    else:
        form = ClientForm()
    return render(request, 'clientes_form.html', {'form':form})

@login_required
def edit_client(request, id):
    client = get_object_or_404(Client, pk = id)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('guitars:index')
    else:
        form = ClientForm(instance=client)
    return render (request, 'clientes_form.html', {'form': form})
    
@login_required
def delete_client(request, id):
    client = get_object_or_404(Client, pk = id)
    client.delete()
    return redirect("guitars:index")


#Vistas para los productos

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('guitars:index')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form':form})

#Agregar stock a un producto que ya existe (no funciona esta hvd)

""" def add_stock(request):
    if request.method == 'POST':
        form = ProductStockForm(request.POST)
        if form.is_valid():
            sku = form.cleaned_data['sku']
            quantity = form.cleaned_data['stock']
            
            try:
                # Intenta encontrar el producto por SKU
                product = Product.objects.get(sku=sku)
                # Si el producto existe, actualiza el stock
                product.stock = F('stock') + quantity
                product.save()
                mensaje = f"Stock actualizado para el producto con SKU {sku}. Nuevo stock: {product.stock + quantity}"
            except Product.DoesNotExist:
                # Si el producto no existe, muestra un mensaje de error
                mensaje = f"No se encontró el producto con SKU {sku}. No se puede actualizar el stock."
            
            return render(request, 'error_stock.html', {'mensaje': mensaje})
    else:
        form = ProductStockForm()
    
    return render(request, 'add_stock.html', {'form': form}) """

#Listar productos

def product(request, product_id):
    product = Product.objects.get(pk = product_id)
    template = loader.get_template('display_product.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

class CustomLoginView(LoginView):
    template_name = 'login.html'

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk = id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('guitars:index')
    else:
        form = ProductForm(instance=product)
    return render (request, 'product_form.html', {'form': form})
    
@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk = id)
    product.delete()
    return redirect("guitars:index")