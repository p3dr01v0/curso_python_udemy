class Data:
    def cv_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


# o metodo "__str__" converte de forma automocatica para string, assim não precisamos chamar "print(d1.cv_str())"
# chamamos da seguinte forma "print(d2)" sabendo que d2 recebe a classe Data a função de converter vai se aplicar

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 26
d1.mes = 3
d1.ano = 2024

d2 = Data()
d2.dia = 11
d2.mes = 8
d2.ano = 2023


print(d1.cv_str())
print(d2)
