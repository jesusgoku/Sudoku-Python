import os
from random import randint

CONSOLE_WIDTH = 80
FILAS = 9
COLUMNAS = 9

def generar_matriz(f,c):
    ''' Genera un matriz nula de fxn

    Argumentos:
    f -> (entero) numero de filas
    c -> (entero) numero de columnas

    '''
    A = []
    for i in range(f):
        A.append([0] * c)
    return A

def sudoku_ini_xtablero(A,n):
    ''' Inicializa un tablero de sudoku con n elementos

    Argumentos:
    A -> (lista[9][9]) tablero de sudoku
    n -> (entero) numero de casillas a inicializar, maximo 17

    Retorna:
    A -> (lista[9][9]) tablero de sudoku inicializado
    coords -> (tupla) Con las coordenadas de los elementos fijados

    '''
    coords = []
    n = 17 if n > 17 else n
    while n > 0:
        f = randint(0,8)
        c = randint(0,8)
        val = randint(1,9)
        if A[f][c] == 0:
            error = validar_reglas(A,val,f,c)
            if not error[0]:
                A = fijar_valor(A,val,f,c)
                coords.append((f,c))
                n -= 1
    return A,tuple(coords)

def validar_reglas(A,val,f,c):
    ''' Verifica que se cumplan las reglas del sudoku para un valor dado

    Argumentos:
    A -> (lista[9][9]) es el tablero de juego
    val -> (entero) Corresponde al valor que se desea verificar
    f -> (entero) Corresponde a la coordenada de la fila donde se quiere ubicar
    c -> (entero) Corresponde a la coordenada de la columna donde se quiere ubicar

    '''
    error = False
    errortxt = ''
    # Comprobamos por fila y columna
    for i in range(FILAS):
        # Recorro la fila
        if(A[i][c] == val):
            return True, 'Coincidencia en fila, coordenada ({0}:{1})'.format(i,c)
        if A[f][i] == val:
            return True, 'Coincidencia en columna, coordenada ({0}:{1})'.format(f,i)
    # Comprobamos el cuadrante
    fil_ini_cuad = f - (f % 3)
    col_ini_cuad = c - (c % 3)
    for i in range(fil_ini_cuad,fil_ini_cuad + 3):
        for j in range(col_ini_cuad,col_ini_cuad + 3):
            if A[i][j] == val:
                return True, 'Coincidencia cuadrante, coordenada ({0}:{1})'.format(i,j)
    return error, errortxt

def fijar_valor(A,val,f,c):
    ''' Guarda el valor dado en la fila,columna de la matriz

    Argumentos:
    A -> (lista[9][9]) Matriz en donde se quiere ingresar el valor
    val -> (entero) Valor que se quiere guardar
    f -> (entero) Fila en la que se desea guardar el valor
    c -> (entero) Columna en la que se desea gaurdar el valor

    '''
    A[f][c] = val
    return A

def mostrar_tablero(A,coords):
    ''' Mostrar tablero de sudoku con separacion de cuadrantes
        y numeracion de filas y columas

    Argumentos:
    A -> (lista) Matriz con el tablero de sudoku
    coords -> (tupla) Contiene las coordenadas con valores no editables

    '''
    f = len(A)
    c = len(A[0])
    for i in range(f):
        # Imprimo el numero de cada columna
        if i == 0:
            print '   ',
            for k in range(c):
                if k != 0 and k % 3 == 0:
                    print ' ',k,
                else:
                    print k,
            print ''
        # Imprimo las lineas divisorias horizontales
        if i == 0 or i == 3 or i == 6:
            print '- ' * (c + 5)
        # Imprimo el numero de fila
        print i,
        for j in range(c):
            # Imprimo las lineas divisorias verticales al inicio
            if j == 0 or j == 3 or j == 6:
                print '|',
            # Imprimo el valor de la casilla
            if A[i][j] == 0:
                print 0,
                #if os.name == 'posix':
                #    print chr(27) + '[0;33m' + '0' + chr(27) + '[0m',
                #else:
                #    print '0',
            else:
                if os.name == 'posix':
                    if (i,j) in coords:
                        print chr(27) + '[0;31m' + str(A[i][j]) + chr(27) + '[0m',
                    else:
                        print chr(27) + '[0;32m' + str(A[i][j]) + chr(27) + '[0m',
                else:
                    print A[i][j],
            # Imprimo las lineas divisorias verticales al final
            if j == (c - 1):
                print '|',
        print ''
        # Imprimo la linea delimitadora horizontal al final
        if i == (f - 1):
            print '- ' * (c + 5)

def pedir_comando():
    ''' Pide un comando al usuario

    Retorno:
    entrada -> (cadena) valor introducido por el usuario

    '''
    print 'Opciones:'
    print 'Ingreso coordenada=valor (f,c=valor) sin parentesis'
    print 'Comandos de accion:'
    print '\th) para mostrar instrucciones'
    print '\tr) para reiniciar el tablero'
    print '\ts) para salir'
    entrada = raw_input('Ingrese comando: ')
    return entrada

def permitir_edicion(coords,f,c):
    ''' Valida si se puede editar una coordenada f,c si no esta en coords

    Argumentos:
    coords -> (tupla) lista de coordenadas no editables
    f -> (entero) fila de la coordenada
    c -> (entero) columna de la coordenada
    '''
    return False if (f,c) in coords else True

def estado_tablero(A):
    ''' Verifica que el trablero este completo

    Retorno
    Regresa True si el tablero esta lleno

    '''
    f, c = obtener_dimension(A)
    for i in range(f):
        for j in range(c):
            if A[i][j] == 0:
                return False
    return True

def obtener_dimension(A):
    ''' Devuelve la dimension del arreglo dado

    Argumentos:
    A -> (lista) Lista a la que se le quiere calcular las dimensiones

    Retorno:
    (tupla) con los las filas,columnas

    '''
    return len(A),len(A[0])

if __name__ == '__main__':
    pass
