n1 = float(input())
n2 = float(input())

media = (n1+n2)/2

if 9.0 <= media <= 10.0:
    conceito = 'A'
elif 7.5 <= media < 9.0:
    conceito = 'B'
elif 6.0 <= media < 7.5:
    conceito = 'C'
elif 4.0 <= media < 6.0:
    conceito = 'D'
elif 0.0 <= media < 4.0:
    conceito = 'E'
    
print(n1)
print(n2)
print(media)
print(conceito)

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print('APROVADO')
elif conceito == 'D' or conceito == 'E':
    print('REPROVADO')