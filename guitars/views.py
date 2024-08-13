from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Client, Product, Sale
from guitars.forms import ClientForm, ProductForm, ProductStockForm, SaleForm


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



#Listar productos

def product(request, category_name, id):
    product = get_object_or_404(Product, pk=id)
    template = loader.get_template('display_product.html')
    context = {
        'product': product,
        'category_name': category_name  # Puedes incluir esta variable si necesitas mostrar la categoría en la plantilla
    }
    return HttpResponse(template.render(context, request))


class CustomLoginView(LoginView):
    template_name = 'login.html'

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def edit_product(request, category_name, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('guitars:category_view', category_name=category_name)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form, 'category_name': category_name})

@login_required
def delete_product(request, category_name, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('guitars:category_view', category_name=category_name)


#Filtrar un producto por su categoria

def category_view(request, category_name):
    products = Product.objects.filter(category=category_name)
    return render(request, 'categorias.html', {'products': products, 'category_name': category_name})

#Mostrar todas las categorias

def category_list(request):
    # Obtén una lista de todas las categorías distintas
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'category_list.html', {'categories': categories})


                                                                            
def sale_list(request):                                                   
    sales = Sale.objects.all()                                          	

    return render(request, 'sale_list.html', {'sales':sales})         
                                                                            
                                                                            
@login_required                                                             
def add_sale(request):                                                    
    if request.method == 'POST':                                            
        form = SaleForm(request.POST, request.FILES)                      
        if form.is_valid():                                                 
            form.save()                                                     
            return redirect ('guitars:index')                               
    else:                                                                   
        form = SaleForm()                                                
    return render(request, 'sale_form.html', {'form':form})             
                                                                            
@login_required                                                             
def edit_sale(request, id):                                               
    sale = get_object_or_404(Sale, pk = id)                             
    if request.method == 'POST':                                            
        form = SaleForm(request.POST, request.FILES, instance=sale)     
        if form.is_valid():                                                 
            form.save()                                                     
            return redirect('guitars:index')                                
    else:                                                                   
        form = ClientForm(instance=client)                                  
    return render (request, 'clientes_form.html', {'form': form})           
                                                                            
@login_required                                                             
def delete_sale(request, id):                                             
    sale = get_object_or_404(Sale, pk = id)                             
    sale.delete()                                                         
    return redirect("guitars:index")  
