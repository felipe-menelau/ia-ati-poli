class Servidor:

    def __init__(self, matricula, **kwargs):
        self.matricula = matricula
        self.nome = kwargs['nome']
        self.forca_de_trabalho = self.forca_to_horas(kwargs['forca_de_trabalhos'])
        self.cargo = kwargs['cargo']
        self.funcao = kwargs['funcao']
        self.formacoes = []

    def forca_to_horas(forca):
        forca_str = str(forca)
        results = ''
        counter = 0
        aux1 = ''
        aux2 = ''
        for letras in forca:
            if letra != ':' and counter  == 0:
                results + letra
            if letra != ':' and counter == 1:
                aux1 = aux1 + letra
            if letra != ':' and counter == 2:
                aux2 = aux2 + letra
            else:
                if counter == 0:
                    int(results)
                    counter = counter + 1
                    next
                if counter == 1:
                    int(aux1)
                    counter = counter + 1
                    next
                if counter == 2:
                    int(aux2)
                    results = results + aux1/60 + (aux2/3600)
        return results
