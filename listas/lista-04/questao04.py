arquivo = open(amazon.csv)

for linha in arquivo:
	elementos = linha.split()
	ano = elementos[0]
	estado = elementos[1]
	mes = elementos[2]
	numero = elementos[3]
	data = elementos[4]
	
	queimadas = []
	
	if estado == 'Mato Grosso' and (int(ano) >= 2010):
		queimadas.append(numero)
		total = sum(queimadas)

print(total)