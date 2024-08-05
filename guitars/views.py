from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Client
from guitars.forms import ClientForm


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