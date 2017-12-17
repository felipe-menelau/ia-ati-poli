import pandas as pd
import base64
from models.funcao import Funcao

def read_file_funcao(file_path):
    file_in = open(file_path, 'r')
    resulting_df = pd.read_csv(file_in)
    funcoes = []
    current = None

    for row in resulting_df.iterrows():
        current = Funcao(row[1]['ID']+row[1]['Atribuição']+row[1]['Tamanho Estimado'], id=row[1]['ID'], atribuicao=row[1]['Atribuição'],
                carga_horaria=row[1]['Tamanho Estimado'], funcao=row[1]['Função'], certificacao=row[1]['Certificação'])

        if row[1]['Prática Gerencial'] == 'Sim':
            current.pratica_gerencial = True

        competencies = []
        competencies.append(row[1]['Áreas de Conhecimento\n\n* Ver aba "Áreas de Conhecimento"'])
        competencies.append(row[1]['Unnamed: 5'])
        competencies.append(row[1]['Unnamed: 6'])
        for competency in competencies:
            if str(competency) != 'nan':
                if str(competency) in current.areas_de_conhecimento:
                    current.areas_de_conhecimento[competency] = current.areas_de_conhecimento[competency] + 1
                else:
                    current.areas_de_conhecimento[competency] = 1
        funcoes.append(current)
    return funcoes

