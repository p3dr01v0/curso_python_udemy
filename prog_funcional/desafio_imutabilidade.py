from calendar import mdays, month_name
from locale import setlocale, LC_ALL
from functools import reduce
# print(month_name[1]) passa o mes
# print(mdays[1]) passa quantos dias tem no mes selecionado

setlocale(LC_ALL, 'pt_BR')  # deixa em portugues
# print(month_name[1])  # não é mais em ingles

# a variavel 'mes' faz referencia ao indice, ou seja 'mdays[1]=31' janeiro tem 31 dias
meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
# print(f'os seguintes meses possuem 31 dias: \n', tuple(meses_31))

# pegando o indice dos meses que tem 31 dias, fazemos uso para puxar o nome do mes atraves do numero do indice
# como por exemplo month 'month_name[1]=janeiro'
meses_nomes = map(lambda mes: month_name[mes], meses_31)
# print(list(meses_nomes))


juntar_meses = reduce(lambda txt, nome_mes: f'{
                      txt} \n -{nome_mes}', meses_nomes, 'Meses com 31 dias:')
print(juntar_meses)
