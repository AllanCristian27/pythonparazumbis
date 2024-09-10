# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte aquantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumanteperde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.


cigarros_dia = int(input("Quantidade fumada por dia: "))
anos_fumados = int(input("Quantidade de anos fumados: "))

minutos_perdidos = (cigarros_dia * 10 * anos_fumados * 365)

tempo_perdido = minutos_perdidos / 1444

print(f"Dias perdidos: {tempo_perdido:.0f}")