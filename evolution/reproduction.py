from copy import deepCopy
from random import randint
from models.funcao import Funcao
from models.servidores import Servidor

def regularReproduction(function1, function2):
    functionsSize = len(function1)
    iterator = 0
    newFunctions =[]

    while iterator <= ((functionsSize- 1)/2):
        newFunctions.append(deepCopy(function1[iterator]))
        iterator+=1

    while iterator <= functionsSize-1:
        newFunctions.append(deepCopy(function2[iterator]))
        iterator+=1

    return newFunctions

def randomReproduction(funcao1, funcao2):
    functionsSize = len(function1)
    drawNumber = 0
    visited =[]
    newFunctions = []

    while len(newFunctions) < (functionsSize/2):
        drawNumber = randint(0, functionsSize-1)

        if drawNumber is not in visited:
            visited.append[drawNumber]
            newFunctions.append(deepCopy(function1[drawNumber]))

    while len(newFunctions) < functionsSize:
        drawNumber = randint(0, functionsSize-1)

        if drawNumber is not in visited:
            visited.append[drawNumber]
            newFunctions.append(deepCopy(function2[drawNumber]))
