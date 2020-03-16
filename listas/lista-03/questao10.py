print('Em que turno você estuda?')
turno = input('Digite M se for matutino; V se for vespertino; ou N se for noturno.')

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

