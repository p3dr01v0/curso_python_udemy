#no python não tinha o laço switch até a versão 3.10 que o match foi adicionado
# mas podemos era possivel simular ele da seguinte forma:
#utilizando uma função e  um dicionario
def dia_semana (dia):
    dias ={
        1: 'domingo',
        2: 'segunda',
        3: 'terca',
        4: 'quarta',
        5: 'quinta',
        6: 'sexta',
        7: 'sabado'
    }
    return dias.get(dia, '** valor invalido **')
    
for dia in range(1, 9):
    print(f'{dia}: {dia_semana(dia)}')