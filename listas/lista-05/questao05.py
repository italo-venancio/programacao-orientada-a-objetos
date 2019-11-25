def somaImposto(taxaImposto, custo):
    taxaImposto = (taxaImposto/100)
    soma = (taxaImposto*custo) + custo
    return soma 
taxaImposto = int(input())
custo = int(input())

print(somaImposto(taxaImposto, custo))