<<<<<<< HEAD
# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.


v = float(input("Valor da mercadoria. "))
d = float(input("Percentual de desconto. ")) / 100

valor_desconto =  v * (1+d) - v


print(f"O valor com desconto é de R$ {valor_desconto:.2f} e o desconto e de R$ {v - valor_desconto:.2f}")

=======
p = str(input("Informe uma palavra."))


if p == p[::-1]:
    print("A palavra e palíndromo.")

else:
    print("A palavra não e palíndromo.")
>>>>>>> 6c629cbe037fe77d680619271bacad4912dc3e83

