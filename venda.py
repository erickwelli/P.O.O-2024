class Venda:
    def __init__(self, dataVenda):
        self.produtos = []
        self.dataVenda = dataVenda
        self.total = 0.0

    # Getters
    def get_produtos(self):
        return self.produtos

    def get_dataVenda(self):
        return self.dataVenda

    def get_total(self):
        return self.total

    # Setters
    def set_dataVenda(self, dataVenda):
        self.dataVenda = dataVenda

    # Método para adicionar produto
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.calcular_total()

    # Método para remover produto
    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.get_nome() == nome:
                self.produtos.remove(produto)
                break
        self.calcular_total()

    # Método para calcular o total da venda
    def calcular_total(self):
        self.total = 0.0
        for produto in self.produtos:
            self.total += produto.get_preco() * produto.get_quantidade()
        return self.total