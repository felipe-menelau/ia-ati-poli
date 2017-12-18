class Servidor:

    def __init__(self, matricula, **kwargs):
        self.matricula = matricula
        self.nome = kwargs['nome']
        self.forca_de_trabalho = self.forca_to_horas(kwargs['forca_de_trabalho'])
        self.cargo = kwargs['cargo']
        self.funcao = kwargs['funcao']
        self.formacoes = []
        self.areas_de_conhecimento = {}
        self.forca_de_trabalho_s = self.forca_de_trabalho

    def forca_to_horas(self, forca):
        forca_str = str(forca)
        results = '0'
        counter = 0
        aux1 = '0'
        aux2 = '0'
        for letra in forca:
            if letra != ':' and counter  == 0:
                results = results + letra
            elif letra != ':' and counter == 1:
                aux1 = aux1 + letra
            elif letra != ':' and letra != '.' and counter == 2:
                aux2 = aux2 + letra
            else:
                if counter == 0:
                    results = int(results)
                    counter = counter + 1
                if counter == 1:
                    aux1 = int(aux1)
                    counter = counter + 1

        aux2 = int(aux2)
        results = results + aux1/60 + (aux2/3600)
        return results

    def experiencia_em_gestao(self):
        if "GEST PRO" in self.areas_de_conhecimento:
            return True
        else:
            return False
