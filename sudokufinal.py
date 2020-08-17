#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle
from random import randint
import time
import re
import os
import sys
import sudokulib.gen_sudoku

try:
    import cPickle as pickle
except ImportError:
    pickle

from sudokulib.gen_sudoku import *
from sudokulib.utilidades import *
from sudokulib.printscreen import *
from sudokulib.persistencia import *
from sudokulib.colores import *
from sudokulib.tableros import *

CONSOLE_WIDTH = 80
FILAS = 9
COLUMNAS = 9

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
                            print 'Felicitaciones! haz completado el tablero'
                            mostrar_tablero(tablero)
                            pregunta = pregunta_continuar()
                            if pregunta == 'n':
                                print 'Gracias por jugar! hasta pronto.'
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
