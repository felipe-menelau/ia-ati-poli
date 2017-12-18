from random import randint

def gerar_individuo(servidores, funcoes):
    contagem_servidores = len(servidores)

    for index, funcao in enumerate(funcoes):
        print (str(index) + " de " + str(len(funcoes)))
        #import pdb; pdb.set_trace()
        while funcao.quantidade_slots != 0:
            servidor_selecionado = servidores[randint(0, contagem_servidores-1)]

            quantidade_necessaria = funcao.carga_horaria / funcao.quantidade_slots

            if servidor_selecionado.forca_de_trabalho >= quantidade_necessaria:
                servidor_selecionado.forca_de_trabalho = servidor_selecionado.forca_de_trabalho - funcao.horas_slotadas()
                funcao.carga_horaria = funcao.carga_horaria - funcao.horas_slotadas()

                funcao.servidores_alocados.append(servidor_selecionado)

                funcao.quantidade_slots = funcao.quantidade_slots - 1

    return funcoes
