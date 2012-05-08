#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from .colores import *

def pregunta_continuar():
    ''' Pregunta al usuario si desea continuars
    
    Retorno:
    devuelve 'y' o 'n' segun responda el usuario
    
    '''
    continuarBucle = True
    while continuarBucle:
        pregunta = raw_input('Iniciar otra vez? (y/n): ')
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

def cls():
    ''' Limpia la pantalla en sistemas Unix y Windows, en otros simula
    
    '''
    if(os.name == 'posix'):
        os.system('clear')
    elif(os.name == 'nt'):
        os.system('cls')
    else:
        print '\n' * 80

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

if __name__ == '__main__':
	pass