def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'1) {segundo}')
    print(f'1) {terceiro}')


if __name__ == '__main__':
    podium = {
        'primeiro': 'Hamilton',
        'segundo': 'Verstapen',
        'terceiro': 'Lecrerc'
    }
    resultado_f1(**podium)
