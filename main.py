import pandas as pd
import operator
from random import randint
from sys import argv
from evolution.fitness import fitness_individuo
from evolution.fitness import fitness
from evolution.initial_population import gerar_individuo
from evolution.mutation import mutation
from evolution.reproduction import regularReproduction
from evolution.reproduction import randomReproduction
from parser.parser_funcao import read_file as read_funcao
from parser.parser_servidor import read_file as read_servidor
from copy import deepcopy
##
TARGET = 0.7
RANDOM_WHEN = 0.5
NUMBER_OF_ITERACTIONS = 5000
##

def main():
    funcoes_filename = argv[1]
    servidores_filename = argv[2]

    fitness = {}

    funcoes = read_funcao(funcoes_filename)
    servidores = read_servidor(servidores_filename)

    populacao = []

    for i in range(0, 49):
        print("gerando individuo" + str(i))
        temp_servidores = deepcopy(servidores)
        temp_funcoes = deepcopy(funcoes)
        individuo = gerar_individuo(temp_servidores, temp_funcoes)
        populacao.append(individuo)

    for index, individuo in enumerate(populacao):
        fitness[index] = fitness_individuo(individuo)

    tuplas_fitness_ordenadas = ordenar_fitness(fitness)

    iter_number = 0
    while fitness[tuplas_fitness_ordenadas[0][0]] < TARGET and iter_number <= NUMBER_OF_ITERACTIONS:
        selecionado1 = tuplas_fitness_ordenadas[randint(0, len(tuplas_fitness_ordenadas)-1)][0]
        selecionado2 = tuplas_fitness_ordenadas[randint(0, len(tuplas_fitness_ordenadas)-1)][0]
        pior_fitness = tuplas_fitness_ordenadas[-1][0]
        maior_fitness = tuplas_fitness_ordenadas[0][0]

        if selecionado1 != selecionado2:
            if fitness[maior_fitness] > RANDOM_WHEN:
                filho = randomReproduction(populacao[selecionado2], populacao[selecionado2])
                filho = mutation(filho)
                filho = (filho, fitness_individuo(filho))
                if filho[1] > fitness[pior_fitness]:
                    populacao[pior_fitness] = filho[0]
                    fitness[pior_fitness] = filho[1]
            else:
                filho = regularReproduction(populacao[selecionado2], populacao[selecionado2])
                filho = mutation(filho)
                filho = (filho, fitness_individuo(filho))
                if filho[1] > fitness[pior_fitness]:
                    populacao[pior_fitness] = filho[0]
                    fitness[pior_fitness] = filho[1]

            tuplas_fitness_ordenadas = ordenar_fitness(fitness)
        else:
            pass
        print(str(tuplas_fitness_ordenadas[0][1]) + ' ' + str(tuplas_fitness_ordenadas[-1][1]))
        iter_number +=1
        print (iter_number)

    escrever_resposta(populacao[tuplas_fitness_ordenadas[0][0]])

def escrever_resposta(individuo):
    df_resposta = pd.DataFrame(columns=['Funcao', 'Servidor', 'Fitness'])
    for funcao in individuo:
        if funcao.servidores_alocados != []:
            for servidor in funcao.servidores_alocados:
                df_resposta.loc[-1] = [funcao.chave, servidor.matricula, fitness(funcao)]
                df_resposta.index =  df_resposta.index + 1
        else:
            pass
    df_resposta.to_csv('resposta.csv', sep=',')

def ordenar_fitness(fitness):
    return sorted(fitness.items(), key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    main()
