from django.db import models
from .validation import validar_cedula, validar_correo

class Client(models.Model):
    cedula = models.CharField(max_length=10,  validators = [validar_cedula], null=False)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, validators= [validar_correo], null=False)
    address = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return (f'{self.name}')