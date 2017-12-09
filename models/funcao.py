class Funcao:

    def __init__(self, chave, **kwargs):
        self.chave = chave
        self.id = kwargs['id']
        self.atribuicao = kwargs['atribuicao']
        self.carga_horaria = self.carga_to_hora(kwargs['carga_horaria'])
        self.funcao = kwargs['funcao']
        self.areas_de_conhecimento = {}
        self.certificacao = kwargs.get('certificacao', '')
        self.pratica_gerencial = kwargs.get('pratica_gerencial', False)
        self.quantidade_slots = kwargs.get('quantidade_slots', 1)
        self.servidores_alocado = []

    def __setattr__(self, name, value):
        if name == 'pratica_gerencial' and not isinstance(value, bool):
            raise TypeError("Pratica gerencial must be bool")
        super().__setattr__(name, value)


    def carga_to_hora(self, forca):
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

    def horas_slotadas(self):
        return self.forca_de_trabalho / quantidade_slots

    def esvaziar_alocamento(self):
        self.servidores_alocados = []
        return

