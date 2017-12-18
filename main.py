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
##
TARGET = 0.5
RANDOM_WHEN = 0.7
##

def main():
    funcoes_filename = argv[1]
    servidores_filename = argv[2]

    fitness = {}

    funcoes = read_funcao(funcoes_filename)
    servidores = read_servidor(servidores_filename)

    populacao = []

    for i in range(0, 49):
        individuo = gerar_individuo(servidores, funcoes)
        populacao.append(individuo)

    for index, individuo in enumerate(populacao):
        fitness[index] = fitness_individuo(individuo)

    tuplas_fitness_ordenadas = ordenar_fitness(fitness)

    while fitness[tuplas_fitness_ordenadas[0][0]] < TARGET:
        selecionado1 = tuplas_fitness_ordenadas[randint(0, len(tuplas_fitness_ordenadas))][0]
        selecionado2 = tuplas_fitness_ordenadas[randint(0, len(tuplas_fitness_ordenadas))][0]
        pior_fitness = tuplas_fitness_ordenadas[-1][0]

        if selecionado1 != selecionado2:
            if fitness[maior_fitness] > RANDOM_WHEN:
                filhos = randomReproduction(populacao[selecionado2], populacao[selecionado2])
                filhos = map(lambda filho: mutation(filho), filhos)
                filhos = map(lambda filho: (filho, fitness_individuo(filho)), filhos)
                for filho in filhos:
                    if filho[1] > fitness[pior_fitness]:
                        populacao[pior_fitness] = filho[0]
                        tuplas_fitness_ordenadas[pior_fitness][1], fitness[pior_fitness] = filho[1], filho[1]
            else:
                filhos = regularReproduction(populacao[selecionado2], populacao[selecionado2])
                filhos = map(lambda filho: mutation(filho), filhos)
                filhos = map(lambda filho: (filho, fitness_individuo(filho)), filhos)
                for filho in filhos:
                    if filho[1] > fitness[pior_fitness]:
                        populacao[pior_fitness] = filho[0]
                        tuplas_fitness_ordenadas[pior_fitness][1], fitness[pior_fitness] = filho[1], filho[1]

            tuplas_fitness_ordenadas = ordenar_fitness(fitness)
        else:
            pass

    escrever_resposta(populacao[tuplas_fitness_ordenadas[0][0]])

def escrever_resposta(individuo):
    df_resposta = pd.DataFrame(columns=['Funcao', 'Servidor', 'Fitness'])
    for funcao in individuo:
        df_resposta.loc[-1] = [funcao.funcao, funcao.servidores_alocados[0].matricula, fitness(funcao)]
    df_resposta.to_csv('resposta.csv', sep=',')

def ordernar_fitness(fitness):
    return sorted(fitness.items(), key=operator.itemgetter(1)).reverse()

if __name__ == '__main__':
    main()
