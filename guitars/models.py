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
    
    
class Product(models.Model):
    sku = models.CharField(max_length=10, null=False, unique=True)
    brand = models.CharField(max_length=45, null=False)
    model = models.CharField(max_length=45, null=False)
    color = models.CharField(max_length=20, null=False)
    GUITAR_CATEGORY = {
        ('Guitarras Electricas', 'Guitarras Electricas'),
        ('Guitarras Acusticas', 'Guitarras Acusticas'),
        ('Guitarras Electro Acusticas', 'Guitarras Electro Acusticas'),
        ('Guitarras Clasicas', 'Guitarras Clasicas'),
        ('Bajos', 'Bajos')
    }
    category = models.CharField(max_length=45, choices=GUITAR_CATEGORY, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_selling = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    picture = models.ImageField(upload_to='guitars_images')
    stock = models.IntegerField()
    
    def __str__(self) -> str:
        return (f'{self.brand} {self.model}')



#Modelo de las ventas (hace el calculo total)


#ventas

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.client}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale,  related_name='sale_items',  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} - Cantidad: {self.quantity}"