# myapp/utils.py
from django.forms import ValidationError

#Funcion para validar la cedula
def validar_cedula_ecuatoriana(cedula):
    if len(cedula) != 10:
        return False

    digito_verificador = int(cedula[9])
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0

    for i in range(9):
        valor = int(cedula[i]) * coeficientes[i]
        if valor >= 10:
            valor -= 9
        total += valor

    modulo = total % 10
    digito_calculado = 10 - modulo if modulo != 0 else 0

    return digito_calculado == digito_verificador

def validar_cedula(value):
    if not validar_cedula_ecuatoriana(value):
        raise ValidationError('Cédula ecuatoriana no válida.')
    
    
#Funcion para validar el correo
def validar_correo(value):
    if '@' not in value:
        raise ValidationError('Correo electrónico no válido. Debe contener al menos una arroba (@).')

    