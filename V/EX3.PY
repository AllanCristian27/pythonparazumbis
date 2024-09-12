def par(x):
    if x % 2 ==0:
        return True
    return False


def seven(x):
    if x % 7 == 0:
        return True
    return False

lista = []

for x in range(1066,3628):
    if par(x) and seven(x):
        lista.append(x)

print(len(lista))