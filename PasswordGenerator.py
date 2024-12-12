import random #esto lo que hace es que importa la libreberia random :v y permite que nos de los valores aleatorios para la contraseña 
import string #si quitas esto se va todo alv, esto es para que podamos usar las letras y numeros en la contraseña
# Respuesta a si quiere
Mayusculas = ''
Numeros = ''
Simbolos = ''
while Mayusculas != 'si' and Mayusculas != 'no':
    Mayusculas = (input('Desea incluir mayusculas?: ')).lower()

while Numeros != 'si' and Numeros != 'no':
    Numeros = input('Desea incluir numeros?: ').lower()

while Simbolos != 'si' and Simbolos != 'no':
    Simbolos = input('Desea incluir simbolos?: ').lower()
 

def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros=True, incluir_simbolos=True): #los Def ya sabes que se usan pa definir caracteres, en este caso es de la funcion generar_contraseña
    # Aca vamos a definir los caracteres base
    caracteres = string.ascii_lowercase  # Letras minúsculas

    # Agremamos los caracteres según las opciones 
    if incluir_mayusculas: 
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
        
        #Continuara xD