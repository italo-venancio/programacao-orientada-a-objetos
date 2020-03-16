peso = int(input('Informe o peso de peixes:'))

excesso = peso - 50

multa = excesso*4

print('O excesso é de {} quilos.' .format(excesso))
print('O valor da multa é de R$ {:.2f}.' .format(multa))