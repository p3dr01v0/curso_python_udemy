def dia_semana(dia):
    match dia:
        case 1:
            return 'domingo'
        case 2:
            return 'segunda'
        case 3:
            return 'terca'
        case 4:
            return 'quarta'
        case 5:
            return 'quinta'
        case 6:
            return 'sexta'
        case 7:
            return 'sabado'
        case _:
            return '** valor invalido **'

for dia in range(1,9):
    print(f'{dia}: {dia_semana(dia)}')
