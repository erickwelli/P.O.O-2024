from livro import Livro

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionar_livro(self, livro: Livro):
        self.__livros.append(livro)
        print("O livro {} foi adicionado com sucesso!".format(livro.getTitulo))

    def remover_livro(self, titulo:str):
        for livro in self.__livros:
            if livro.getTitulo() == titulo:
                self.__livros.remove(livro)
                print("O livro {} foi removido com sucesso!".format(titulo))
        