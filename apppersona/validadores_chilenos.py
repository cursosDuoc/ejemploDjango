from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_chilean_rut(rut):
    """
    valida que un rut chileno sea valido, para ser usado
    por django en los modelos y formularios.
    Esto no retorna NADA. 
    Pero cuando el rut no es valido, lanza un Error.
    ( modelo de excepciones )
    """
    if validar_rut(rut) == False :
        raise ValidationError(
            _('El rut "%(valor)s" no es válido'),
            code='invalid',
            params={'valor' : rut }
        )


def validar_rut(rut):
    rut_por_partes = rut.split('-')
    if not rut_por_partes[0].isnumeric() :
        return False
    rut_como_int = int(rut_por_partes[0])
    dv_calculado = calcular_dv_rut(rut_como_int)
    dv_ingresado = rut_por_partes[1]
    if dv_calculado == dv_ingresado.upper() :
        return True
    return False

def calcular_dv_rut(rut_sin_dv) :
    """
    Calcula el digito verificador del rut chileno de acuerdo
    al algoritmo del registro civil.
    ver detalles en https://es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario
    """
    contador = 2
    suma = 0
    while rut_sin_dv != 0 :
        multiplo = (rut_sin_dv % 10) * contador 
        suma = suma + multiplo
        rut_sin_dv = rut_sin_dv // 10 # OJO division entera, sin decimales
        contador = contador + 1
        if contador == 8 :
            contador = 2
    digito = 11 - (suma % 11)
    if digito == 10 :
        dv = 'K'
    elif digito == 11 :
        dv = '0'
    else :
        dv = str(digito)
    return dv

