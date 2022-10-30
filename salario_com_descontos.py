ganho_por_hora = float(input("Informe seu ganho por hora:"))
quantidade_de_horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas neste mês:"))

salario_bruto = ganho_por_hora * quantidade_de_horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (ir +inss + sindicato)


print("+ Salário Bruto : R$ {:.2f}".format(salario_bruto))
print("- IR (11%) : R$ {:.2f}".format(ir))
print("- INSS (8%) : R$ {:.2f}".format(inss))
print("- Sindicato ( 5%) : R$ {:.2f}".format(sindicato))
print("= Salário Liquido : R$ {:.2f}".format(salario_liquido))