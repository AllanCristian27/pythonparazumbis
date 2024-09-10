salario_bruto = float(input(" Informe o salário bruto."))

inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - inss - ir - sindicato

print(f" Salário liqúido: R$ {salario_liquido:.2f}\n INSS: R$ {inss:.2f} \n IR: R$ {ir:.2f} \n Sindicato: R$ {sindicato:.2f} ",)
