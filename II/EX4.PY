n1 = float(input("Informe um número. "))
n2 = float(input("Informe um número. "))
n3 = float(input("Informe um número. "))


if n1 > n2 and n1 > n3:
    print(f"O maior e o {n1}")

elif n2 > n1 and n2 > n3:
    print(f"O maior e o {n2}")

elif n3 > n2 and n3 > n2:
    print(f"O maior o {n3}")

else:
    print("Os valores são iguais.")
