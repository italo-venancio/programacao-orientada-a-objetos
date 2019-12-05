import random
nomes = ["Nicole", "Victor", "Emilia", "Leonardo", "Tarsila", "Pedro", "Margarete", "Lauro", "Beatriz", "Hugo", "Isadora", "Lucas", "Catarina", "Celso", "Helena", "Gentil", "Iracema", "Fausto", "Guiomar", "Ivan"]
sobrenomes = ["Pereira", "Guerra", "Flores", "Rivera", "Pena", "Garcia", "Monteiro", "Azevedo", "Santana", "Alencar", "Silva", "Calabresa", "Queiroz", "Palhares", "Martins", "Lima", "Frangipane", "Mendes", "Freitas", "Alegria"]
N = int(input())

with open("gente.txt", "w") as saida:
    for x in range(0, N):
        nome = (random.choice(nomes))
        sobrenome = (random.choice(sobrenomes))
        idade = random.randint(0, 101)
        print(nome, sobrenome, idade, file = saida)
        