def peso_homens(h):
    return (72.7*h)-58

def peso_mulheres(h):
    return (62.1*h)-44.7

g = input('Informe o gênero:')
h = float(input('Informe a altura:'))

if g == 'masculino':
    print(peso_homens(h))
elif g == 'feminino':
    print(peso_mulheres(h))
