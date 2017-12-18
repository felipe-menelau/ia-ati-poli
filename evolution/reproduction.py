from copy import deepcopy
from random import randint
from models.funcao import Funcao
from models.servidores import Servidor

def regularReproduction(function1, function2):
    functions_size = len(function1)
    iterator = 0
    new_functions =[]

    while iterator <= ((functions_size- 1)/2):
        new_functions.append(deepcopy(function1[iterator]))
        iterator+=1

    while iterator <= functions_size-1:
        new_functions.append(deepcopy(function2[iterator]))
        iterator+=1

    return new_functions

def randomReproduction(function1, function2):
    functions_size = len(function1)
    draw_number = 0
    visited =[]
    new_functions = []

    while len(new_functions) < (functions_size/2):
        draw_number = randint(0, functions_size-1)

        if draw_number not in visited:
            visited.append(draw_number)
            new_functions.append(deepcopy(function1[draw_number]))

    while len(new_functions) < functions_size:
        draw_number = randint(0, functions_size-1)

        if draw_number not in visited:
            visited.append(draw_number)
            new_functions.append(deepcopy(function2[draw_number]))

    return new_functions
