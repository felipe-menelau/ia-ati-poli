NUMERO_MAX_MUTACOES = 20
from random import randint
from evolution.fitness import fitness
from models.funcao import Funcao
from models.servidores import Servidor

def mutation(some_allocation):
    number_of_mutations = randint(1, NUMERO_MAX_MUTACOES)
    while (number_of_mutations > 0):
        random_function_1 = randint(0, len(some_allocation)-1)
        random_function_2 = randint(0, len(some_allocation)-1)

        first_function = some_allocation[random_function_1]
        second_function = some_allocation[random_function_2]

        if first_function.servidores_alocados and second_function.servidores_alocados:
            first_servers = first_function.servidores_alocados
            second_servers = second_function.servidores_alocados

            random_server_1 = randint(0, len(first_servers)-1)
            random_server_2 = randint(0, len(second_servers)-1)

            if str(second_function.funcao) != 'nan' and str(first_function.funcao) != 'nan':
                if (((first_servers[random_server_1].cargo in second_function.funcao) or
                    (first_servers[random_server_1].funcao in second_function.funcao) and
                    (second_servers[random_server_2].cargo in first_function.funcao) or
                    (second_servers[random_server_2].funcao in first_function.funcao)) and
                     first_servers[random_server_1].experiencia_em_gestao() or
                     first_servers[random_server_1].experiencia_em_gestao() == second_function.pratica_gerencial and
                     second_function.horas_slotadas() == first_function.horas_slotadas() or
                     second_function.horas_slotadas() <= first_function.horas_slotadas() + first_function.carga_horaria_s or
                     first_function.horas_slotadas() <= second_function.horas_slotadas() + second_function.carga_horaria_s and
                     first_function.servidores_alocados != [] and second_function.servidores_alocados != [] ):

                    temporary_holder = first_servers[random_server_1]

                    first_servers[random_server_1] = second_servers[random_server_2]
                    second_servers[random_server_2] = temporary_holder

                    first_function.servidores_alocados = first_servers
                    second_function.servidores_alocados = second_servers

                    some_allocation[random_function_1] = first_function
                    some_allocation[random_function_2] = second_function

            number_of_mutations -=1

    return some_allocation
