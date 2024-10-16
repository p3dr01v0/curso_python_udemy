class Data:
    # declaramos o construtor como __init__, não é possivel ter mais que um construtor, toda vez que a classe Data
    # for chamada as funções dentro dela serão executadas
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(26, 3, 2024)
# d1.dia = 26
# d1.mes = 3
# d1.ano = 2024

d2 = Data(11, 8, 2023)
# d2.dia = 11
# d2.mes = 8
# d2.ano = 2023

print(f'{d1}\n{d2}')

d3 = Data()
print(d3)
