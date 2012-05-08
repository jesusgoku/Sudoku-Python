#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from .colores import *
from .utilidades import *

CONSOLE_WIDTH = 80

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

if __name__ == '__main__':
	pass