valor_por_hora = int(input('Quanto você ganha por hora?')) 
num_de_horas = int(input('Qual o número de horas trabalhadas no mês?'))

salario_bruto = valor_por_hora*num_de_horas

INSS = (salario_bruto*(8/100))

sindicato = (salario_bruto*(5/100))

IR = (salario_bruto*(11/100))

salario_liquido = salario_bruto - INSS - sindicato - IR

print('Salário bruto: R$ {:.2f}' .format(salario_bruto))
print('INSS: R$ {:.2f}' .format(INSS))
print('Sindicato: R$ {:.2f}' .format(sindicato))
print('Salário líquido: R$ {:.2f}' .format(salario_liquido))