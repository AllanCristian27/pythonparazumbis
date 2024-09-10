n1 = int(input("DIVIDENDO. "))
n2 = int(input("DIVISOR. "))
d  = n1 % n2

while d != 0:
    n1 = n2
    n2 = d
    d = n1 % n2

print(n2)

