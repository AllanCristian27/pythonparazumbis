def two(x):
    for i in x:
        if i in "2":
            return True
    return False

def seven(x):
    for i in x:
        if i in "7":
            return True
    return False

lista = []

for x in range(18643,33086):
    if two(str(x)) and not seven(str(x)):
        lista.append(x)

print(len(lista))