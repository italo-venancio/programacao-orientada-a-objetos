def extenso(data):
    DD = int(data[0])
    MM = int(data[1])
    AAAA = int(data[2])

    if MM == 1:
        MM = 'janeiro'
    elif MM == 2:
        MM = 'fevereiro'
    elif MM == 3:
        MM = 'março'
    elif MM == 4:
        MM = 'abril'
    elif MM == 5:
        MM = 'maio'
    elif MM == 6:
        MM = 'junho'
    elif MM == 7:
        MM = 'julho'
    elif MM == 8:
        MM = 'agosto'
    elif MM == 9:
        MM = 'setembro'
    elif MM == 10:
        MM = 'outubro'
    elif MM == 11:
        MM = 'novembro'
    elif MM == 12:
        MM = 'dezembro'
    print('{} de {} de {}' .format(DD, MM, AAAA))


data = input().split()
extenso(data)
