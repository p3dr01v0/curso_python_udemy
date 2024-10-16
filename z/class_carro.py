class Carro:
    def __init__(self, velocidade_max):
        self.maxima = velocidade_max
        self.atual = 0

    def aclerar(self, delta=5):
        velocidade = self.atual + delta
        self.atual = velocidade if velocidade <= self.maxima else self.maxima
        return self.atual

    def frear(self, delta=5):
        velocidade = self.atual - delta
        self.atual = velocidade if velocidade >= 0 else 0
        return self.atual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(f'acelerando: {c1.aclerar(8)}')

    print('\n')

    for _ in range(10):
        print(f'freando: {c1.frear(20)}')
