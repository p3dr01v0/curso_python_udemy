class Carro:
    def __init__(self, velocidade_max):
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidade_max
        velocidade = self.velocidade_atual + delta
        self.velocidade_atual = velocidade if velocidade <= maxima else maxima
        return self.velocidade_atual

    def frear(self, delta=5):
        velocidade = self.velocidade_atual - delta
        self.velocidade_atual = velocidade if velocidade > 0 else 0
        return self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(f'aceleracao atual: {c1.acelerar(8)}')

    print('\n\n')

    for _ in range(10):
        print(f'frenagem atual: {c1.frear(delta=20)}')
