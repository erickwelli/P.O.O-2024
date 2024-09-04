from autor import Autor
from livro import Livro
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    while True:
        print("\nMenu da Biblioteca")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Buscar Livro")
        print("4. Listar Livros")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade do autor: ")
            data_nascimento = input("Data de nascimento do autor (DD/MM/AAAA): ")
            ano_publicacao = int(input("Ano de publicação: "))

            autor = Autor(nome_autor, nacionalidade, data_nascimento)
            livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionar_livro(livro)

        elif escolha == "2":
            titulo = input("Título do livro a ser removido: ")
            biblioteca.remover_livro(titulo)

        elif escolha == "3":
            titulo = input("Título do livro a ser buscado: ")
            biblioteca.buscar_livro(titulo)

        elif escolha == "4":
            biblioteca.listar_livros()

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()