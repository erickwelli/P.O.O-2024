from base import Fase
from util import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao = ''' A aventura começa!
        Ao chegar em um hospital abandonado, você encontra 
'''
        self.__opcoes = []

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte2()
        else:
            return Parte3()


class Parte3(Fase):
    def __init__(self):
        self.__descricao = '''
'''

class Parte4(Fase):

    def executar(self):
        print('''Você tenta entrar, mas não consegue
              Você tenta entrar pelo duto de ar
              mas nao aguenta seu peso. Você cai e morre!
               ''')

        return None
    

class Parte5(Fase):

    def executar(self):
        print('''Você segue para a ala de cirurgia.
              Lá você encontra o remédio na estante!
               ''')

        return None
    

class Parte6(Fase):

    def executar(self):
        print('''Você se depara com diversos expermentos com pessoas.
              Lá você cai em uma armadilha e morre!
               ''')

        return None
    
class Parte7(Fase):

    def executar(self):
        print('''Você encontra o remédio na gaveta da mesa!
               ''')

        return None
    