from datetime import date 

#Dada una fecha de nacimiento en formato YYYY-MM-DD
#devuelve la edad
def calcularEdad(cumple):
    fechActual = date.today() 
    try:
        edad = fechActual.year - cumple.year - ((fechActual.month, fechActual.day) < (cumple.month, cumple.day))
        return edad
    except ValueError:
        return -1

#Dado el numero de años trabajados en condiciones peligrosas
#devuelve el descuento a la edad de jubilacion
def calcularDescuento(tiempo):
    x = tiempo//4
    if x >= 5:
        return 5
    return x

#Codigo para validar si la persona aplica a una pension
#segun lo definido en Ley del Seguro Social
def aplicaPensionIVSS(sexo,horasAcreditadas,fechaDeNacimiento,condicionesPeligrosas):
    temp = fechaDeNacimiento.split('-', 3)
    try:
        edad  = calcularEdad(date(int(temp[0]), int(temp[1]), int(temp[2])))
    except ValueError:
        return False
    descuentoDeAnos = calcularDescuento(condicionesPeligrosas)

    if horasAcreditadas >= 750:
        if sexo == 'F' and edad >= (55 - descuentoDeAnos):
            return True
        elif sexo == 'M' and edad >= (60 - descuentoDeAnos):
            return True
    return False