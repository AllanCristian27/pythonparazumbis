N1 = float(input("Informe às medidas dos lados. "))
N2 = float(input("Informe às medidas dos lados. "))
N3 = float(input("Informe às medidas dos lados. "))

if N1 == N2 and N1 == N3 and N2 == N3:
    print("EQUILÁTERO.")
elif N1 != N2 and N1 != N3 and N2 != N3:
    print("ESCALENO.")    
else:
    print("ISÓSCELES.")


    