import pandas as pd
from random import randint
from syste import argv
from evolution.fitness import fitness
from evolution.initial_population import gerar_individuo
from evolution.mutation import mutation
from evolution.reproduction import regularReproduction
from parser.parser_funcao import read_file as read_funcao
from parser.parser_servidor import read_file as read_servidor


def main():
    funcoes_filename = argv[1]
    servidores_filename = arvg[2]

    valor_aceitavel = 0.8
    fitness_populacao = 0
    fitness = 0

    funcoes = read_funcao(funcoes_filename)
    servidores = read_servidor(servidores_filename)

    populacao = gerar_individuo(servidores, funcoes)
    random_function_1 = randint()
    random_function_2 = randint(0, random_function_1)
    populacao_reproduzida = regularReproduction(individuos[random_function_1], individuos[random_function_2])

    while fitness_populacao < valor_aceitavel or fitness < valor_aceitavel:

        for individuo in populacao:
            obj = fitness(individuo)
            fitness += obj['fitness']

        for individuo_reproduzido in populacao_reproduzida:
            obj = fitness(individuo_reproduzido)
            fitness_populacao += obj['fitness']


