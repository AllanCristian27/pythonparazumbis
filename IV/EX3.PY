import random

lista_1 = random.sample(range(0,100),10)
lista_2 = random.sample(range(0,100),10)

lista = []


for x in lista_1:
    lista.append(x)
    for x in lista_2:
        lista.append(x)


print(lista)   
    