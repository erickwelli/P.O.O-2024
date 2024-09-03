from autor import Autor
class Livro:
    def __init__(self, titulo:str, autor:Autor, anoPublicacao:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoPublicacao = anoPublicacao

    def setTitulo(self, titulo):
        if titulo == str:
            self.__titulo = titulo

    def setAutor(self):
        self.__autor

    def setAnoPublicacao(self):
        self.__anoPublicacao
        
    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor

    def getAnoPublicacao(self):
        return self.__anoPublicacao