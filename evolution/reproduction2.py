#Renomeia o arquivo reproduction.py que já tem no gh pra individual.py, pra não dar conflito com essa aqui

import copy
from random import randint
from models.funcao import Funcao
from models.servidores import Servidor

def regularReproduction(function1, function2):
	#Both of the vector have the same size, so get the value of one random value 
	functionsSize = len(function1)
	iterator = 0
	newFunctions =[] 
	
	# Adds the parent one's data to the now array. If the size is odd, takes the size/2+1
	while iterator <= ((functionsSize- 1)/2):
		newFunctions.append(copy.deepCopy(function1[iterator]))
		iterator+=1

	#Does the same with the data from the array 2
	while iterator <= functionsSize-1:
		newFunctions.append(copy.deepCopy(function2[iterator]))
		iterator+=1

	#return new array of funcoes
	return newFunctions

def randomReproduction(funcao1, funcao2):
	#Gets the size of the first array
	functionsSize = len(function1)
	drawNumber = 0
	visited =[]
	newFunctions = []

	#while the new array doesn't have the desired value, keeps trying to insert values in it
	while len(newFunctions) < (functionsSize/2):
		drawNumber = randint(0, functionsSize-1)
		
		if drawNumber is not in visited:
			visited.append[drawNumber]
			newFunctions.append(copy.deepCopy(function1[drawNumber]))
	
	#Same thing with the other array
	while len(newFunctions) < functionsSize:
		drawNumber = randint(0, functionsSize-1)
		
		if drawNumber is not in visited:
			visited.append[drawNumber]
			newFunctions.append(copy.deepCopy(function2[drawNumber]))