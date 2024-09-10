kg_peixe = float(input("Informe o peso."))

if kg_peixe > 50: 
    multa = (kg_peixe - 50)  * 4
    print(f" Multa de R$ {multa:.2f}")
else:
    print("Não houve multa. ")    

