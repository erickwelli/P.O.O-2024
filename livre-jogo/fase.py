from base import Fase
from util import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao = ''' Bem-Vindos ao jogo Doll Charm! Vamos começar nossa aventura:
        É um domingo à noite, estar a nevar. Você chegou em casa após passar um dia agradável com seus amigos. Ao entrar, retirar seus sapatos, pega uma xícara de café e liga a TV no seu seriado. Após um tempo, é cortado para os comerciais onde aparece uma fábrica de bonecas "Doll Charm", que fabricavam bonecas de porcelana, o anúncio é cortado por uma queda de energia.Você desempregado, não conseguiu pagar as contas, incluindo a de luz. Logo após a queda, escuta batidas frenéticas em sua porta, ao atender, é um dos agiotas que você deve, ele enfurecido pelos atrasos e juros grandes, te obriga a trabalhar nesta fábrica que o mesmo era sócio, ele lhe deu o prazo de uma semana cravada, para pagar tudo, caso você não fosse trabalhar na fábrica e escolhesse outro meio ou então era o seu fim. Antes de dormir você…
'''
        self.__opcoes = ["Pesquisar sobre a fábrica", "Ir ná fábrica na segunda-feira"]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte2()
        else:
            return Parte3()


class Parte2(Fase):
    def __init__(self):
        self.__descricao = '''Você decide pesquisar sobre a fábrica em seu computador, o relógio marca 23h e 49min e você inicia a pesquisa. Ao pôr o nome da fábrica, apareceu relacionado a uma página de blog de teorias assombrosas… Curioso, você abre a página e fica entretido por horas. Ao olhar o relógio, já está a marcar 3h da manhã e você reflete se realmente vai querer ir à fábrica depois de ter visto as teorias assustadoras.'''
        self.__opcoes = ["Desistir de ir", "Ir mesmo assim"]

        def executar(self):
            print(\nParte2)
            print(self.__descricao)
            JogoUtil.exibir_opcoes(self._)

class Parte3(Fase):
    def __init__(self):
        self.__descricao = '''Você tem certeza disso?'''


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
    