from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s no es un numero par',
            params={'value': value}
        )

def validar_nombre_categoria(value):
    if value == 'No permitido':
        raise ValidationError("No es una opcion permitida")

def validar_texto(value):
    if len(value) == 1:
        raise ValidationError("El texto introducido es muy corto")

def validar_positivo(value):
    if value <= 0:
        raise ValidationError(
            '%(value)s debe ser un mayor cero 0',
            params={'value': value}
        )