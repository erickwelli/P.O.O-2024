from produto import Produto
from venda import Venda

def menu():
    venda = None
    while True:
        print("\nMenu:")
        print("1. Criar nova venda")
        print("2. Adicionar produto à venda")
        print("3. Remover produto da venda")
        print("4. Listar produtos da venda")
        print("5. Mostrar total da venda")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            data = input("Digite a data da venda (dd/mm/yyyy): ")
            venda = Venda(data)
            print("Venda criada com sucesso.")

        elif opcao == '2':
            if venda is None:
                print("Por favor, crie uma venda primeiro.")
            else:
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                produto = Produto(nome, preco, quantidade)
                venda.adicionar_produto(produto)
                print("Produto adicionado com sucesso.")

        elif opcao == '3':
            if venda is None:
                print("Por favor, crie uma venda primeiro.")
            else:
                nome = input("Digite o nome do produto a ser removido: ")
                venda.remover_produto(nome)
                print("Produto removido com sucesso.")

        elif opcao == '4':
            if venda is None:
                print("Por favor, crie uma venda primeiro.")
            else:
                print("Produtos na venda:")
                for produto in venda.get_produtos():
                    print(f"Nome: {produto.get_nome()}, Preço: {produto.get_preco()}, Quantidade: {produto.get_quantidade()}")

        elif opcao == '5':
            if venda is None:
                print("Por favor, crie uma venda primeiro.")
            else:
                total = venda.calcular_total()
                print(f"Total da venda: {total:.2f}")

        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()