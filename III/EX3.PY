a = 80000
b = 200000

c = 0

while a < b:
    a = a *(1.03)
    b = b *(1.015)
    c = c + 1

print(int(a))
print(int(b))
print(c)

