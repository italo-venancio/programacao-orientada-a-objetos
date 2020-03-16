valor_da_hora = int(input())
quantidade_de_horas = int(input())

salario_bruto = valor_da_hora*quantidade_de_horas

if salario_bruto <= 900:
    IR = salario_bruto*(0)
elif 900 < salario_bruto <= 1500:
    IR = salario_bruto*(5/100)
elif 1500 < salario_bruto <= 2500:
    IR = salario_bruto*(10/100)
elif 2500 < salario_bruto:
    IR = salario_bruto*(20/100)
    
INSS = salario_bruto*(10/100)
FGTS = salario_bruto*(11/100)
salario_liquido = salario_bruto-IR-INSS

print('Salário Bruto: R$ {:.2f}' .format(salario_bruto))
print('IR: R$ {:.2f}' .format(IR))
print('INSS: R$ {:.2f}' .format(INSS))
print('FGTS: R$ {:.2f}' .format(FGTS))
print('Total de descontos: {:.2f}' .format(IR+INSS))
print('Salário Liquido: R$ {:.2f}' .format(salario_liquido))