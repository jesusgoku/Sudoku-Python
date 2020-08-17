#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import cPickle as pickle
except ImportError:
    pickle

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
    A -> (lista) Tablero de sudoku guardado
    coords -> (tupla) pares de coordenadas no editables

    '''
    fp = open('partida.dat','r')
    datos = pickle.load(fp)
    A = datos[0]
    coords = datos[1]
    return A, tuple(coords)
