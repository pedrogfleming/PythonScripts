#importar libreria con funciones matematicas
from math import *

print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

character_name = "Tom"
character_age = 19.454
character_location = "Argentina"
isMale = True
print("-----------Trabajando variables--------------")
print("Mi nombre es "+character_name.upper()+",\n"
   "Tengo "+str(character_age)+" años,\n"
    "Vivo en "+character_location+".")
print(len(character_location))
print(character_location[0])
print(character_location.index("gen"))
print(character_location.replace("tina","zuela"))
print("-----------Trabajando numeros--------------")
#trabajando con numeros

my_num = 4
my_negativeNum = -10
print(3+4)
print(10%2)
print(str(my_num)+" es mi numero favorito")
print(abs(my_negativeNum))
print(pow(2,4))

print("-----------Trabajando con inputs--------------")

nombre_Usuario = input("Ingrese su nombre : ")
edad_Usuario = input("Ingrese su edad : ")
print("Hola "+nombre_Usuario+"!\nTu edad es: "+edad_Usuario)

print("A continuacion, operara la calculadora")
num1 = input("Ingrese el primer numero : ")
num2 = input("Ingrese el segundo numero :")
result = float(num1)+float(num2)
print(result)