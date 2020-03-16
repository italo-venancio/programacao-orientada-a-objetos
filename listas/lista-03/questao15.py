lados = input().split()
a = float(lados[0])
b = float(lados[1])
c = float(lados[2])

if (a >= (b+c)) or (b >= (a+c)) or (c >= (a+b)):
    print('Não forma triângulo.')
    
else:
    if a==b==c:
        print('Triângulo Equilátero.')
        
    elif (a==b != c) or (a==c != b) or (b==c != a):
        print('Triângulo Isósceles.')
    
    else:
        print('Triângulo Escaleno.')