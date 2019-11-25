def digitos(numero):
    numero = str(numero)
    lista = []
    
    for x in numero:
        lista.append(1)
    
    quantidade = (sum(lista))
    print(quantidade)

n = int(input())
digitos(n)


