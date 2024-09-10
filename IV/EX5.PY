texto = '''
The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()


texto = texto.replace(","," ")
texto = texto.replace("."," ")
texto = texto.replace(":"," ")


texto = texto.split()

lista = []



def pytonica(x):
    for a in x:
        if a in "python":
            return True

    return False


for x in texto:
    if len(x) > 4 and pytonica(x):
        lista.append(x)
        

print(lista)
print(len(lista))



 