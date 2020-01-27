from datetime import date 

#Dada una fecha de nacimiento en formato YYYY-MM-DD
#devuelve la edad
def calcularEdad(cumple): 
    fechActual = date.today() 
    edad = fechActual.year - cumple.year - ((fechActual.month, fechActual.day) < (cumple.month, cumple.day))
    return edad

#Codigo para validar si la persona aplica a una pension
#segun lo definido en Ley del Seguro Social
def aplicaPensionIVSS(sexo,horasAcreditadas,fechaDeNacimiento,condicionesPeligrosas):
    temp = fechaDeNacimiento.split('-', 3)
    edad  = calcularEdad(date(int(temp[0]), int(temp[1]), int(temp[2])))

    if sexo == 'F' and edad >= 55:
        return True
    elif sexo == 'M' and edad >= 60:
        return True
    return False