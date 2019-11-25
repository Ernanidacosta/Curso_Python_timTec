class Proposicao:
    def __init__(self, nome, ementa):
        self._nome = nome
        self._ementa = ementa
    
    def menciona_termo(self, termo):
        return termo in self._ementa

    def getNome(self):
        return self._nome

    def getEmenta(self):
        return self._ementa

    def setNome(self, nome):
        pass

    def setEmenta(self, ementa):
        pass

    def __str__(self):
        return "Nome: {}\n Ementa: {}", format(self.nome, self.ementa)

    nome = property(fget=getNome, fset=setNome)
    ementa = property(fget=getEmenta, fset=setEmenta)