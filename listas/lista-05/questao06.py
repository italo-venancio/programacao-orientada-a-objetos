def conversor(horas):
    if horas < 12:
        horario = 'A.M'
    elif horas >= 12:
        horario = 'P.M'
    
    if horas > 12:
        horas -= 12
    return(horas, horario)
    
def saida(horas, minutos):
    
    print('{}:{} {}' .format(horas, minutos, horario))

entrada = input().split()
horas = int(entrada[0])
minutos = int(entrada[1])

saida(conversor(horas), minutos)