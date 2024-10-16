def semana(dia):
    dias = {
        1: 'final de semana',
        2: 'dia de semana',
        3: 'dia de semana',
        4: 'dia de semana',
        5: 'dia de semana',
        6: 'dia de semana',
        7: 'final de semana',
    }
    return dias.get(dia, '**valor invalido **')
    
for dia in range (1, 9):
    print(f'{dia}: tipo: {semana(dia)}')