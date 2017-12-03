import pandas as pd
from models.servidores import Servidor

def read_file(file_path):
    file_in = open(file_path, 'r')
    resulting_df = pd.read_csv(file_in)
    servidores = []
    current = None

    for row in resulting_df.iterrows():
        if str(row[1]['Matrícula']) != 'nan':
            if current != None:
                servidores.append(current)
            current = Servidor(row[1]['Matrícula'], nome=row[1]['Nome'], forca_de_trabalho=row[1]['Força de Trabalho'], cargo=row[1]['Cargo'],
                        funcao=row[1]['Função'])
        current_formation = (row[1]['Tipo de Qualificação\n\n* Ver aba "Tipo de Qualificação"'], row[1]['Nome.1'])
        current.formacoes.append(current_formation)
        competencies = []
        competencies.append(row[1]['Áreas de Conhecimento\n\n* Ver aba "Áreas de Conhecimento"'])
        competencies.append(row[1]['Unnamed: 10'])
        competencies.append(row[1]['Unnamed: 11'])
        for competency in competencies:
            if str(competency) != 'nan':
                if str(competency) in current.areas_de_conhecimento:
                    current.areas_de_conhecimento[competency] = current.areas_de_conhecimento[competency] + 1
                else:
                    current.areas_de_conhecimento[competency] = 1
    return servidores
