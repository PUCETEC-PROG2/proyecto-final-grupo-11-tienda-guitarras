from django.db import models
from django.forms import ValidationError
from .validation import validar_cedula, validar_correo

class Client(models.Model):
    cedula = models.CharField(max_length=10,  validators = [validar_cedula], null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, validators= [validar_correo], null=False)
    address = models.CharField(max_length=100, null=False)
    
    def clean(self):
        super().clean()
        if Client.objects.filter(cedula=self.cedula).exists():
            raise ValidationError({'cedula': 'Ya existe un cliente con esta cédula.'})

    
    def __str__(self) -> str:
        return (f'{self.name}')