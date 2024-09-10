m = float(input("M³ "))

quantidade_latas = m / 54
valor_gasto = quantidade_latas * 80

if quantidade_latas < 1:
    quantidade_latas = 1
    valor_gasto = 80
    print(f"Será necessario {quantidade_latas} lata, e custara R$ {valor_gasto:.2f}.")
else:
    print(f"Serão necessarios {quantidade_latas} latas, e custara R$ {valor_gasto:.2f}.")

