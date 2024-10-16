class Carro:
    def acelerar(self, aceleracao):
        velocidade = aceleracao
        lista = [aceleracao]
        while velocidade < 180:
            velocidade = velocidade + aceleracao
            lista.append(velocidade)
            lista[-1] = 180 if lista[-1] > 180 else lista[-1]
        return lista

    def frear(self, delta):
        freio = 180
        lista = []
        while freio >= 0:
            freio = freio - delta
            lista.append(freio)
            lista[-1] = 0 if lista[-1] < 0 else lista[-1]
        return lista


if __name__ == '__main__':
    c1 = Carro()

    print(f'aceleracao atual: {c1.acelerar(aceleracao=8)})')

    print(f'frenagem atual: {c1.frear(delta=20)}')
