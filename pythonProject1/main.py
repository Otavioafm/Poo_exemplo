
class Pessoa:
    def __init__(self,nome:str,gmail:str,idade:int):
        self.__nome=nome
        self.__idade=idade
        self.__gmail=gmail
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def gmail(self):
        return self.__gmail

class Livros:
    def __init__(self,titulo:str,autor:str,disponibilidade:bool,restricaoIdade:int):
        self.__titulo=titulo
        self.__autor=autor
        self.__disponibilidade=disponibilidade
        self.__restricaoIdade=restricaoIdade
    @property
    def titulo(self):
        return self.__titulo
    @property
    def autor(self):
        return self.__autor
    @property
    def disponibilidade(self):
        return self.__disponibilidade
    @property
    def restricaoIdade(self):
        return self.__restricaoIdade



















