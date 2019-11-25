def enesima(n):
    linha = 0
    lista = []
    elemento = 1

    while linha < n:
        lista.append(elemento)
        print(lista)
        linha += 1
        elemento += 1

n = int(input())
enesima(n)