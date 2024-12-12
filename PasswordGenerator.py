import random
import string

Contraseña = ''
Longitud = int(input('Que longitud desea que tenga?: '))
Contra = string.ascii_lowercase
mayusculas = ''
numeros = ''
simbolos = ''

while mayusculas != 'si' and mayusculas != 'no':
    mayusculas = input('Quieres mayusculas?: ')
while numeros != 'si' and numeros != 'no':
    numeros = input('Quieres numeros?: ')
while simbolos != 'si' and simbolos != 'no':
    simbolos = input('Quieres simbolos?: ')

if mayusculas == 'si':
    Contra += string.ascii_uppercase
if numeros == 'si':
    Contra += string.digits
if simbolos == 'si':
    Contra += string.punctuation

for i in range(Longitud):
    Contraseña += Contra[random.randrange(len(Contra))]

print(Contraseña)