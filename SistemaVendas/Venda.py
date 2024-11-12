import json
import Produto

class Venda:
    def __init__(self, dataVenda):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos
        
    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

    def adicionarProduto(self, produto):
        self.__produtos.append(produto)
        print(f'Produto {produto.get_nome()} adicionado com sucesso! ')

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")

    def SalvarEmJson(self, arquivo):
        objeto_dic = [obj.to_dic() for obj in self.__produtos]
        dados_json = json.dumps(objeto_dic)
        with open (arquivo, 'w') as arquivo:
            arquivo.write(dados_json)  

    def RecuperarDados(self, arquivo):
        with open(arquivo, 'r', encoding="utf-8") as f:
            carregar_dic = json.load(f)
        for dados in carregar_dic:
            objeto = Produto.from_dic(dados)
            self.adicionarProduto(objeto)
            