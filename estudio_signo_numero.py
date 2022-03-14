#Funcion que estudia el signo de un numero

def signo_numero(n):
    if n < 0:
        print('Este numero es negativo')
    elif n > 0:
        print('Este numero es positivo')
    else:
        print('El numero es 0, no tiene signo')
