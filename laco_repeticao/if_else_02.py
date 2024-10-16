def faixa_etaria():
    if 0 <= idade < 18:
        return 'menor de idade'
    # no range o valor vai de primeiro numero até o ultimo numero -1 abaixo vai de 19 ate 64, o 65 não conta
    elif idade in range(19, 65):
        return 'maior de idade'
    elif idade in range(65, 100):
        return 'idade idosa'
    elif idade > 100:
        return 'idade centenaria'
    else:
        return 'valor invalido'


if (__name__ == '__main__'):
    for idade in (13, 34, 56, 79, 68, 99, 103, -2):
        print(f'para a idade de {idade} {faixa_etaria()}')
