nota = int(input('digite a nota: '))


def help():
    print('digite um valor valido')

if (__name__ == '__main__'):

    if (nota > 10 ):
        help()
        
    elif(nota >= 9.1):
        print('nota em letra: A')
        
    elif(nota >= 8.1):
        print('nota em letra: A-')
        
    elif(nota >= 7.1):
        print('nota em letra: B')
        
    elif(nota >= 6.1):
        print('nota em letra: B-')
        
    elif(nota >= 5.1):
        print('nota em letra: C')
        
    elif(nota >= 5.1):
        print('nota em letra: C-')
        
    elif(nota >= 4.1):
        print('nota em letra: D')
        
    elif(nota >= 3.1):
        print('nota em letra: D-')
        
    elif(nota >= 2.1):
        print('nota em letra: E')
        
    elif(nota >= 1.1):
        print('nota em letra: E-')
        
    elif(nota >= 0):
        print('nota em letra: A')
        
    elif(nota < 0):
        help()
        