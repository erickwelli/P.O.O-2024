class Autor:
    def __init__(self, nome:str, nacionalidade:str, dataNascimento:str):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__dataNascimento = dataNascimento

    def setNome(self, nome):
        if nome == str:
            self.__nome = nome

    def setNacionalidade(self, nacionalidade):
        if nacionalidade == str:
            self.__nacionalidade = nacionalidade

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
        

    def getNome(self):
        return self.__nome
    
    def getNacionalidade(self):
        return self.__nacionalidade
    
    def getDataNascimento(self):
        return self.__dataNascimento
    
    def exibirAutor(self):
        return ("Autor: {} \nNacionalidade: {} \nData de Nascimento: {}".format(self.__nome, self.__nacionalidade, self.__dataNascimento))