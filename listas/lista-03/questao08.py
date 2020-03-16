prod1 = int(input('Informe o preço do produto 1:'))
prod2 = int(input('Informe o preço do produto 2:'))
prod3 = int(input('Informe o preço do produto 3:'))

if prod1 < prod2 and prod1 < prod3:
    print('Você deve comprar o produto 1.')
elif prod2 < prod1 and prod2 < prod3: 
    print('Você deve comprar o produto 2.')
elif prod3 < prod1 and prod3 < prod2:
    print('Você deve comprar o produto 3.')