from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

#Login
class CustomLoginView(LoginView):
    template_name = 'login.html'