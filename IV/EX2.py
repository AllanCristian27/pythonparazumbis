import random


lista = random.sample(range(1,100),20)
par = []
impar = []


for x in lista:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print("Pares:",par)
print("Impares:",impar)
print(lista)

