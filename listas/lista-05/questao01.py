def enesima(n):
    elemento = 1
    lista = []
    while elemento <= n:
        for x in (1, elemento+1):
            lista.append(elemento)
        print(lista)
        for y in (1, elemento+1):
            lista.pop()
        elemento += 1

numero = (int(input()))
(enesima(numero))
    