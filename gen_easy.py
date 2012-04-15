# -*- coding: utf-8 -*-

import random

fp = open('easy50.txt','r')
nLineas = 0
for i in fp:
    nLineas +=1

nSudokus = nLineas / 10
nSudoku = random.randint(0,nSudokus)
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

print lineas