#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle
from random import randint
import time
import re
import os
import sys
import gen_sudoku

try:
    import cPickle as pickle
except ImportError:
    pickle

CONSOLE_WIDTH = 80
FILAS = 9
COLUMNAS = 9


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
    
def sudoku_ini_xcuadrante(A,n,c):
    ''' Inicia el trablero de sudoku A con n casillas en c cuadrantes
    
    Argumentos:
    A -> (lista[9][9]) tablero de sudoku
    n -> (entero) numero de casillas por cuadrante
    c -> (entero) numero de cuadrantes
    
    '''
    pass

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

def mostrar_matriz(A):
    ''' Muestra matriz en bruto
    
    Argumentos:
    A -> (lista) Matriz que se desea mostrar
    
    '''
    f = len(A)
    c = len(A[0])
    for i in range(f):
        for j in range(c):
            print A[i][j],
        print ''

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

def pedir_coord(msj):
    ''' Pide Coordenada al usuario con
    
    '''
    continuarBucle = True
    while continuarBucle:
        val = raw_input(msj)
        try:
            val = int(val)
        except ValueError:
            print str_color('Error, debe ser un entero entre 0-8',1)
        else:
            if val >= 0 and val <= 8:
                continuarBucle = False
            else:
                print str_color('Error, debe ser un entero entre 0-8',1)
    return val

def pedir_valor():
    continuarBucle = True
    while continuarBucle:
        val = raw_input('Dame el valor: ')
        try:
            val = int(val)
        except ValueError:
            print str_color('Error, debe ser un entero entre 0-9 (-1 salir)',1)
        else:
            if val >= -1 and val <= 9:
                continuarBucle = False
            else:
                print str_color('Error, debe ser un entero entre 0-9 (-1 salir)',1)
    return val

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

def obtener_dimension(A):
    ''' Devuelve la dimension del arreglo dado
    
    Argumentos:
    A -> (lista) Lista a la que se le quiere calcular las dimensiones
    
    Retorno:
    (tupla) con los las filas,columnas
    
    '''
    return len(A),len(A[0])
    
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

def instrucciones():
    ''' Imprime las instrucciones del juego
    
    '''
    cls()
    print '=' * CONSOLE_WIDTH
    print 'SUDOKU'.center(CONSOLE_WIDTH)
    print '=' * CONSOLE_WIDTH
    print ''
    print ' 1.- El juego es un tablero de 9x9 celdas'
    print ' 2.- Dividido en cuadrantes de 3x3 celdas llamados cuadrantes'
    print ' 3.- Cada casilla puede tomar valores del 1-9'
    print ' 4.- Siguiendo las siguientes reglas:'
    print ''
    print '\ta) El numero debe ser unico en su fila'
    print '\tb) El numero debe ser unico en su columna'
    print '\tc) El numero debe ser unico en su cuadrante'
    print ''
    print ' 5.- Las coordenadas estan dadas por valores del 0-8'
    print ' 6.- Puedes salir en cualquier momento ingresando s'
    print ' 7.- Puedes reiniciar la partida ingresando r'
    print ' 8.- Puedes ver estas instrucciones ingresando h'
    print ' 9.- Para borrar una celda ingresa 0 como valor'
    print '10.- Significado color numeros en tablero:'
    print ''
    print '\ta) Rojo: Numeros entregados por el tablero, no editables.'
    print '\tb) Verde: Numeros ingresados por el usuario.'
    raw_input('\nPresiona enter para comenzar...')
    
def pregunta_continuar():
    ''' Pregunta al usuario si desea continuars
    
    Retorno:
    devuelve 'y' o 'n' segun responda el usuario
    
    '''
    continuarBucle = True
    while continuarBucle:
        pregunta = raw_input('ÀIniciar otra vez? (y/n): ')
        if pregunta == 'y' or pregunta == 'n':
            continuarBucle = False
        else:
            print str_color('Respuesta no valida, intentalo otra vez',1)
    return pregunta
        
def pausa():
    ''' Introduce una pausa en el programa
    
    '''
    raw_input('Presionar enter para continuar...')
    
def msj_error(msj):
    ''' Muestra el msj destacado
    
    Argumentos:
    msj -> (cadena) Mensaje de error
    
    '''
    msjLen = len(msj)
    fijar_color(1)
    print '=' * (msjLen + 4)
    print '|' + '-- ERROR --'.center(msjLen + 2) + '|'
    print '=' * (msjLen + 4)
    print '|' + msj.center(msjLen + 2) + '|'
    print '=' * (msjLen + 4)
    reset_color()
    
def permitir_edicion(coords,f,c):
    ''' Valida si se puede editar una coordenada f,c si no esta en coords
    
    Argumentos:
    coords -> (tupla) lista de coordenadas no editables
    f -> (entero) fila de la coordenada
    c -> (entero) columna de la coordenada
    '''
    return False if (f,c) in coords else True
    
def logo_sudoku():
    ''' Muestra el logo del juegos
    
    '''
    cls()
    fijar_color(2)
    print "                                           ,----..          ,--.               "
    print "  .--.--.                     ,---,       /   /   \     ,--/  /|               "
    print " /  /    '.          ,--,   .'  .' `\    /   .     : ,---,': / '         ,--,  "
    print "|  :  /`. /        ,'_ /| ,---.'     \  .   /   ;.  \:   : '/ /        ,'_ /|  "
    print ";  |  |--`    .--. |  | : |   |  .`\  |.   ;   /  ` ;|   '   ,    .--. |  | :  "
    print "|  :  ;_    ,'_ /| :  . | :   : |  '  |;   |  ; \ ; |'   |  /   ,'_ /| :  . |  "
    print " \  \    `. |  ' | |  . . |   ' '  ;  :|   :  | ; | '|   ;  ;   |  ' | |  . .  "
    print "  `----.   \|  | ' |  | | '   | ;  .  |.   |  ' ' ' ::   '   \  |  | ' |  | |  "
    print "  __ \  \  |:  | | :  ' ; |   | :  |  ''   ;  \; /  ||   |    ' :  | | :  ' ;  "
    print " /  /`--'  /|  ; ' |  | ' '   : | /  ;  \   \  ',  / '   : |.  \|  ; ' |  | '  "
    print "'--'.     / :  | : ;  ; | |   | '` ,/    ;   :    /  |   | '_\.':  | : ;  ; |  "
    print "  `--'---'  '  :  `--'   \;   :  .'       \   \ .'   '   : |    '  :  `--'   \ "
    print "            :  ,      .-./|   ,.'          `---`     ;   |,'    :  ,      .-./ "
    print "             `--`----'    '---'       by             '---'       `--`----'     "
    fijar_color(3)
    if os.name == 'posix':
        print '            (           (                )      )       '.center(80)
        print '            )\ )        )\ )  (       ( /(   ( /(       '.center(80)
        print '   (   (   (()/(    (  (()/(  )\ )    )\())  )\())   (  '.center(80)
        print '   )\  )\   /(_))   )\  /(_))(()/(   ((_)\ |((_)\    )\ '.center(80)
        print '  ((_)((_) (_))  _ ((_)(_))   /(_))_   ((_)|_ ((_)_ ((_)'.center(80)
        print ' _ | || __|/ __|| | | |/ __| (_)) __| / _ \| |/ /| | | |'.center(80)
        print "| || || _| \__ \| |_| |\__ \   | (_ || (_) | ' < | |_| |".center(80)
        print ' \__/ |___||___/ \___/ |___/    \___| \___/ _|\_\ \___/ '.center(80)
    else:
        print '..:: JESUSGOKU ::..'
    reset_color()
    print ''
    pausa()
    
def cls():
    ''' Limpia la pantalla en sistemas Unix y Windows, en otros simula
    
    '''
    if(os.name == 'posix'):
        os.system('clear')
    elif(os.name == 'nt'):
        os.system('cls')
    else:
        print '\n' * 80
        
def guardar_partida(A,coords):
    ''' Guarda la partida con el modulo pickle
    
    Argumentos:
    A -> (lista) Tablero sudoku a guardar
    coords -> (tupla) pares de coordenadas con valores no editables
    
    '''
    datos = [A,coords]
    fp = open('partida.dat','w')
    pickle.dump(datos,fp)
    fp.close()
    
def cargar_partida():
    ''' Cargar una partida guardada
    
    Retorno:
    A -> (lista) Tabler de sudoku guardado
    coords -> (tupla) pares de coordenadas no editables
    
    '''
    fp = open('partida.dat','r')
    datos = pickle.load(fp)
    A = datos[0]
    coords = datos[1]
    return A, tuple(coords)

def pregunta_yn(pregunta):
    ''' Pregunta al usuario dando la posibilidad de responder y/n
    
    Argumentos:
    pregunta -> (cadena) Pregunta que desea que responda el usuario
    
    Retorna:
    respuesta -> (caracter) Valor de la respuesta
    
    '''
    continuarBucle = True
    while continuarBucle:
        respuesta = raw_input(pregunta + ' (y/n): ')
        if(respuesta == 'y' or respuesta == 'n'):
            continuarBucle = False
        else:
            print str_color('Opcion incorrecta, intentalo nuevamnete',1)
    return respuesta

def fijar_color(color):
    ''' Fijar el color de la consola a color
    
    Argumentos:
    color -> (entero) Uno de los siguientes codigos de colores:
    0 -> Negro
    1 -> Rojo
    2 -> Verde
    3 -> Cafe
    4 -> Azul
    5 -> Purpura
    6 -> Cyan
    7 -> Blanco
    
    '''
    if(os.name == 'posix'):
        if(color >= 0 and color <= 7):
            #print chr(27) + '[0;3' + str(color) + 'm',
            sys.stdout.write(chr(27) + '[0;3' + str(color) + 'm')

def reset_color():
    ''' Vuelve los colores por defecto
    Solo funciona en sistemas Unix
    
    '''
    if(os.name == 'posix'):
        #print chr(27) + '[0m',
        sys.stdout.write(chr(27) + '[0m')

def print_color(texto,color):
    ''' Mostrar texto en color
    
    Argumentos:
    texto -> (cadena) Texto a mostrar en color
    color -> (entero) Color en que se mostrar el texto
    
    '''
    fijar_color(color)
    sys.stdout.write(str(texto))
    reset_color()
    
def str_color(cadena,color):
    ''' Devuelve una cadena con marcas de color si se puede
    
    Argumentos:
    cadena -> (cadena) Cadena a devolver con color
    color -> (entero) Uno de los siguientes codigos de colores:
    0 -> Negro
    1 -> Rojo
    2 -> Verde
    3 -> Cafe
    4 -> Azul
    5 -> Purpura
    6 -> Cyan
    7 -> Blanco
    
    '''
    if os.name == 'posix':
        return chr(27) + '[0;3' + str(color) + 'm' + cadena + chr(27) + '[0m'
    else:
        return cadena
    
    
def sudoku_ini_extern():
    ''' Inicializa el sudoku con un algoritmo externo de generacion de sodokus
    
    Retorno:
    A -> (lista) Tablero con valores iniciales
    B -> (tupla) Pares de coordenas con valores no editables
    
    '''
    sudoku = gen_sudoku.makepuzzle(gen_sudoku.solution([None] * 81))
    A = []
    coords = []
    for i in range(len(sudoku)):
        if i % 9 == 0:
            fila = []
        #sudoku[i] = 0 if sudoku[i] == None else sudoku[i]
        if sudoku[i] == None:
            sudoku[i] = 0
        else:
            coords.append((i/9, i % 9))
        fila.append(sudoku[i])
        if len(fila) == 9:
            A.append(fila)
    return A,tuple(coords)
    
def sudoku_ini_file():
    ''' Inicializa un sudoku a partir de un archivo con 50 sudokus pre-echos
    
    Retorno:
    lineas -> (lista[9][9]) tablero de sudoku
    coords -> (tupla) pares de coordenas con valores distintos de 0
    
    '''
    fp = open('easy50.txt','r')
    nLineas = 0
    for i in fp:
        nLineas +=1
    
    nSudokus = nLineas / 10
    nSudoku = randint(0,nSudokus)
    lineaInicio = nSudoku * 10
    
    fp.seek(0)
    nLinea = 0
    lineas = []
    while True:
        linea = fp.readline()
        if not linea:
            break
        if(nLinea >= lineaInicio and nLinea <= lineaInicio + 8):
            lineas.append(linea)
        nLinea += 1
        
    fp.close()
        
    lineas = [linea.strip() for linea in lineas]
    lineas = [list(linea) for linea in lineas]
    for i in range(len(lineas)):
        for j in range(len(lineas[0])):
            lineas[i][j] = int(lineas[i][j])
            
    coords = generar_coords(lineas)
    return lineas,coords

def generar_coords(A):
    ''' A partir de una matriz devuelve una tupla con los pares de coordenadas
        que tienen un valor dintinto de 0
        
    Argumentos:
    A -> (lista[9][9]) Matriz de dos dimensiones con el sudoku
    
    Retorno:
    Tupla con los pares de coordenadas no editables
    
    '''
    coords = []
    f = len(A)
    c = len(A[0])
    for i in range(f):
        for j in range(c):
            if A[i][j] != 0:
                coords.append((i,j))
    return tuple(coords)
    
def input_re():
    ''' Pide al usuario un valor y valida que cumpla con las reglas de
        coordenada o comando
    
    Retorno:
    valor ingresado por el usuario
    '''
    continuarBucle = True
    while continuarBucle:
        print 'Opciones:'
        print 'Ingreso coordenada=valor (f,c=valor) sin parentesis'
        print 'Comandos de accion:'
        print '\th -> para mostrar instrucciones'
        print '\tr -> para reiniciar el tablero'
        print '\ts -> para salir'
        entrada = raw_input('Ingrese comando: ')
        if re.match('(([0-8],[0-8]=[0-9])|(h|s|r))',entrada):
            continuarBucle = False
        else:
            print str_color('Error, comando no valido',1)
    return entrada

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

def creditos():
    ''' Imprime los creditos del programa
    
    '''
    cls()
    fijar_color(2)
    print '\n' * 80
    print '- Creado para -'.center(CONSOLE_WIDTH)
    print 'Fundamentos de programacion'.center(CONSOLE_WIDTH)
    print ''
    time.sleep(1)
    print ''
    print '- Profesora - '.center(CONSOLE_WIDTH)
    print 'Francia Jimenez'.center(CONSOLE_WIDTH)
    print ''
    time.sleep(1)
    print ''
    print '- Bibliografia -'.center(CONSOLE_WIDTH)
    print ''
    time.sleep(1)
    print ''
    print 'Introduccion a la Programacion en Python'.center(CONSOLE_WIDTH)
    print 'Andres Marsal, Isabel Gracia'.center(CONSOLE_WIDTH)
    print ''
    time.sleep(1)
    print 'Python para todos'.center(CONSOLE_WIDTH)
    print 'Raul Gonzalez Duque'.center(CONSOLE_WIDTH)
    print ''
    time.sleep(1)
    print ''
    print '- Creado por -'.center(CONSOLE_WIDTH)
    print 'JesusGoku'.center(CONSOLE_WIDTH)
    print ''
    time.sleep(1)
    print ''
    print '2012 JesusGoku Inc. Algunos derechos reservados...'.center(CONSOLE_WIDTH)
    print 'Viva el Software Libre!'.center(CONSOLE_WIDTH)
    print ''
    time.sleep(1)
    print ''
    print '"Como quisiera que hoy supieras lo que te puede traer paz,'.center(CONSOLE_WIDTH)
    print 'pero esto ahora esta oculto a tus ojos."'.center(CONSOLE_WIDTH)
    print 'Lucas 19:42'.center(CONSOLE_WIDTH)
    print ''
    time.sleep(1)
    print ''
    print '"Mira que te mando que te esfuerzes y seas valiente,'.center(CONSOLE_WIDTH)
    print 'No temas ni desmayes, por que Jehova tu Dios'.center(CONSOLE_WIDTH)
    print 'esta contigo a donde quiera que vayas."'.center(CONSOLE_WIDTH)
    print 'Josue 1:9'.center(CONSOLE_WIDTH)
    print ''
    reset_color()
    

# PROGRAMA PRINCIPAL
if __name__=='__main__':
    logo_sudoku()
    instrucciones()
    tablero = None
    if os.path.exists('partida.dat'):
        cls()
        if(pregunta_yn('Existe una partida guardada, desea cargarla?') == 'y'):
            tablero, coordenadas = cargar_partida()
    if tablero == None:
        tablero = generar_matriz(FILAS,COLUMNAS)
        #tablero, cuadrantes = sudoku_ini(tablero)
        tablero, coordenadas = sudoku_ini_xtablero(tablero,4)
        #tablero, coordenadas = sudoku_ini_extern()
        #tablero, coordenadas = sudoku_ini_file()
    while True:
        cls()
        mostrar_tablero(tablero,coordenadas)
        entrada = pedir_comando()#input_re()
        if entrada == 's':
            #print 'Te has dado por vencido?'
            if(pregunta_yn('Desea guardar su partida?') == 'y'):
                guardar_partida(tablero,coordenadas)
            creditos()
            break
        elif entrada == 'r':
            tablero = generar_matriz(FILAS,COLUMNAS)
            tablero, coordenadas = sudoku_ini_xtablero(tablero,4)
            #tablero, coordenadas = sudoku_ini_extern()
            #tablero, coordenadas = sudoku_ini_file()
            instrucciones()
        elif entrada == 'h':
            instrucciones()
        elif entrada == 'c':
            creditos()
            pausa()
        elif re.match('^[0-8],[0-8]=[0-9]$',entrada):
            f = int(entrada[0])
            c = int(entrada[2])
            val = int(entrada[4])
            if not permitir_edicion(coordenadas,f,c):
                msj_error('No puedes editar este valor')
                pausa()
            else:
                if val == 0:
                    tablero = fijar_valor(tablero,val,f,c)
                else:
                    error = validar_reglas(tablero,val,f,c)
                    if error[0]:
                        msj_error(error[1])
                        pausa()
                    else:
                        tablero = fijar_valor(tablero,val,f,c)
                        completo = estado_tablero(tablero)
                        if completo:
                            print 'ÁFelicitaciones! haz completado el tablero'
                            mostrar_tablero(tablero)
                            pregunta = pregunta_continuar()
                            if pregunta == 'n':
                                print 'ÁGracias por jugar! hasta pronto.'
                                break
                            else:
                                tablero = generar_matriz(FILAS,COLUMNAS)
                                tablero, coordenadas = sudoku_ini_xtablero(tablero,4)
                                #tablero, coordenadas = sudoku_ini_extern()
                                #tablero, coordenadas = sudoku_ini_file()
                                instrucciones()
        else:
            print str_color('Error, comando no valido',1)
            pausa()