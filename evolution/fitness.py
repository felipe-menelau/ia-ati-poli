import pandas as pd
# Globals #
# Idealmente em variaveis de ambient/vindos do db
PESO_GERENCIAL = 1
PESO_CARGA_HORARIA = 1
PESO_CONHECIMENTO = 1
# End Globals #

def fitness(funcao):
    servidores_alocados = funcao.servidores_alocados
    results = pd.DataFrame(columns = ['servidor', 'funcao', 'fitness'])
    fitness = 0

    for servidor in servidores_alocados:
        parametro_gerencial = calcular_parametro_gerencial(servidor, funcao)
        parametro_de_carga_horaria = calcular_parametro_de_carga_horaria(servidor, funcao)
        parametro_de_conhecimento = calcular_parametro_de_conhecimento(servidor, funcao)

        denominador_fitness = (parametro_gerencial*PESO_GERENCIAL +
                                parametro_de_carga_horaria*PESO_CARGA_HORARIA +
                                parametro_de_conhecimento*PESO_CONHECIMENTO)

        numerador_fitness = PESO_GERENCIAL + PESO_CARGA_HORARIA + PESO_CONHECIMENTO
        fitness = denominador_fitness/float(numerador_fitness)

    return fitness

def calcular_parametro_gerencial(servidor, funcao):
    if servidor.experiencia_em_gestao() == funcao.pratica_gerencial:
        return 1
    else:
        return 0


def calcular_parametro_de_carga_horaria(servidor, funcao):
    return (funcao.carga_horaria_s - funcao.carga_horaria)/float(funcao.carga_horaria_s)

def calcular_parametro_de_conhecimento(servidor, funcao):
    match_servidor = 0
    for conhecimento, peso in servidor.areas_de_conhecimento.items():
        if conhecimento in funcao.areas_de_conhecimento:
            match_servidor += 1
    if len(funcao.areas_de_conhecimento.keys()) != 0:
        return float(match_servidor)/float(len(funcao.areas_de_conhecimento.keys()))
    else:
        return 0

def fitness_individuo(individuo):
    todos_fitness = []
    for funcao in individuo:
        todos_fitness.append(fitness(funcao))
    return sum(todos_fitness)/float(len(todos_fitness))
