from livro import Livro

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionar_livro(self, livro: Livro):
        self.__livros.append(livro)
        print("O livro {} foi adicionado com sucesso!".format(livro.getTitulo))

    def remover_livro(self, titulo: str):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                self.__livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

    def buscar_livro(self, titulo: str):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                print("Livro encontrado:")
                print(f"Título: {livro.get_titulo()}")
                print(f"Autor: {livro.get_autor().get_nome()}")
                print(f"Ano de Publicação: {livro.get_ano_publicacao()}")
                return livro
        print(f"Livro '{titulo}' não encontrado na biblioteca.")
        return None

    def listar_livros(self):
        if not self.__livros:
            print("A biblioteca está vazia.")
        else:
            print("Lista de livros na biblioteca:")
            for livro in self.__livros:
                print(f"Título: {livro.get_titulo()} | Autor: {livro.get_autor().get_nome()} | Ano: {livro.get_ano_publicacao()}")