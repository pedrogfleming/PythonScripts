numeros_suerte = [4,8,15,16,23,42]
amigos = ["Kevin", "Karen", "Jim", "Osvaldo", "Oscar"]
print(amigos)
amigos[0] = "Mike"
print(amigos)
print(amigos[1:4])

#Agrego una lista a otra
amigos.extend((numeros_suerte))
print(amigos)
#Agrego un elemento a la lista
amigos.append("Creed")
print(amigos)
#Agrego un elemento en un determinado indice
amigos.insert(2,"Fabian")
print(amigos)
amigos.remove("Jim")
print(amigos)
#Ordenar la lista
numeros_suerte.sort()
print(numeros_suerte)
numeros_suerte.reverse()
print(numeros_suerte)
#Copiar listas
numeros2 = numeros_suerte.copy();
print(numeros2)