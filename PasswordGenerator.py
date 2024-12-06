#tratare de explicar todo en comentarios pa que entiendas cualquier vaina xD 
import random #esto lo que hace es que importa la libreberia random :v y permite que nos de los valores aleatorios para la contraseña 
import string #si quitas esto se va todo alv, esto es para que podamos usar las letras y numeros en la contraseña
def generar_contraseña(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True): #los Def ya sabes que se usan pa definir caracteres, en este caso es de la funcion generar_contraseña
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