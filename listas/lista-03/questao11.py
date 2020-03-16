salario = float(input())

if salario <= 280.00:
    novo_salario = salario + (salario*(20/100))
    print(salario)
    print('20%')
    print(salario*(20/100))
    print(novo_salario)
    
elif 280.00 < salario <= 700.00:
    novo_salario = salario + (salario*(15/100))
    print(salario)
    print('15%')
    print(salario*(15/100))
    print(novo_salario)

elif 700.00 < salario <= 1500.00:
    salario += (salario*(10/100))
    print(salario)
    print('10%')
    print(salario*(10/100))
    print(novo_salario)
    
elif 1500.00 < salario:
    salario += (salario*(5/100))
    print(salario)
    print('5%')
    print(salario*(5/100))
    print(novo_salario)