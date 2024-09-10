import random

lista = random.sample(range(1,100),10)


maior = 0
menor = 100


for x in lista:
    if x < menor :
        menor = x 
    elif x > maior:
        maior = x

print(f"O maior número é {maior} é o menor {menor}.")
print(lista)





 