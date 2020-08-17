#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def fijar_color(color):
    ''' Fijar el color de la consola a color

    Argumentos:
    color -> (entero) Uno de los siguientes códigos de colores:
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
    color -> (entero) Uno de los siguientes códigos de colores:
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
