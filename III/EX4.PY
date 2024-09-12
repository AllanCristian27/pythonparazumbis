n1 = 1
n2 = 1
n3 = 0


n = int(input("Fibonacci. "))


for x in range(n):
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    print(n3)
    

