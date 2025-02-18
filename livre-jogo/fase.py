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
        self.__opcoes = ["desistir de ir", "ir mesmo assim"]

    def executar(self):
        print("\nParte2")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Final_alternativo1()
        
        else:
            return Parte4()


class Final_alternativo1(Fase):

    def executar(self):
        print('''Com sua pele em arrepios e o frio na espinha, iludido pelas terríveis teorias, fechou os olhos em negação e preferiu encontrar um meio de conseguir dinheiro. Ao amanhecer, se dirigiu ao centro comercial a procura de vagas, recebendo vários nãos, estar em pleno ano 2000 e ser jovem, é uma luta entre a fome, luxos e sobrevivência. Atordoado, mal percebe a semana correr, ao olhar o calendário… Sexta-feira, é o último dia que você deveria ter pago os 106 mil reais que estava a dever caso não tivesse se entregado para ir trabalhar na fábrica de bonecas. Aos prantos cai a chorar no chão de sua sala empoeirada, embriagado pelo desgosto e dificuldade social de se estabilizar ou conseguir o básico, a luz fraca da rua decai sobre você, pela janela de vidro. O tempo se passa e a porta é aberta, ao olhar de ombros é seu cobrador, e a morte ao seu lado. Descarado e covardemente você recebe um disparo nas costas, seu corpo esfria, agonizando cai no chão, manchando seu tapete com seu sangue. E assim é deixado lá, jogado sem chances de implorar, antes de sua alma partir apenas escuta o cobrador dizer “A dívida nem foi paga a metade”.
               ''')

        return None
    
class Parte3(Fase):
    def __init__(self):
        self.__descricao = """Você tem certeza disso?"""
        self.__opcoes = ["sim"]

    def executar(self):
        print("\nParte3")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte4
        
class Parte4(Fase):
    def __init__(self):
        self.__descricao = """Segunda de manhã logo cedo, você já se encontra na fábrica, o local aparenta ser confortável, mas há cartazes de bonecas que deixam arrepios, em uma das salas de fileiras e fileiras de bonecas para concerto. Como segurança, você tem tarefas a fazer, vamos começar!"""
        self.__opcoes = ["continuar"]

    def executar(self):
        print("\nParte4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte5
        
class Parte5(Fase):
    def __init__(self):
        self.__descricao = """Na sala de segurança você tem um breve acesso às câmeras de segurança, algumas estão apresentando problemas de conexão frequentemente, então poupe energia, e tem o seu armário, dê uma olhada lá, você não teve.. nunca… trabalhar de mãos vazias. O dia se passa, ao averiguar seu relógio de pulso, já marcava 22:00, Os funcionários já se retiraram e só sobrou você, como marcado no seu quadro de tarefas, deve sair da sala e fechar as portas das salas principais, ao abrir o pequeno armário, encontrou uma lanterna, walkie talkie, e surpreso você pega uma glock 17, com seu carregador cheio… Você nunca teve contado com armas e está surpreso com isso.  Itens pegos, fechou seu armário, a ideia em sua mente era olhar as câmeras e pega o chaveiro para sair, mas seu corpo gela ao ver uma boneca olhando o fundo de sua alma pelo vidro… num flash ela não estava mais lá e você apenas vê seu pequeno vulto percorrer ligeiramente as câmeras."""
        self.__opcoes = ["ir atras da boneca", "ficar na sala de seguranca"]

    def executar(self):
        print("\nParte5")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte6
        
        else:
            return Parte7
        

class Parte7(Fase):
    def __init__(self):
        self.__descricao = """Com frio na barriga, você opta por ficar na sala de segurança, seguro né? Com as mãos trêmulas, é surpreendido por uma queda de energia repentina.
        Dica: Leve a lanterna, não há luzes!
        Agora relutante contra seu medo, fora da sala, segue uma trilha de laços de fita, é uma forma de identidade visual que a fábrica tem, essa trilha leva ao gerador, nada agradável, uma porta de metal e um sinalizador de luz vermelho acima dela, mesma luz que clareava seu semblante."""
        self.__opcoes = ["entrar na sala"]

    def executar(self):
        print("\nParte7")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Final_alternativo2
                

class Final_alternativo2(Fase):
    def executar(self):
        print("""Dica: Cuidado! piso molhado!
              
              	Entrando na pequena sala úmida, você olha em volta, uma alavanca vermelha lhe chama atenção, uma pequena placa diz “cuidado, gerador de energia, risco de descarga elétrica”, era exatamente onde você deveria acionar para energia voltar. Ao puxar a alavanca, estando meio pesada e enferrujada, seu esforço faz com que você e alavanca caiam no chão, desacreditado com a alavanca em mãos você olha para os lados a procura de o que pode fazer agora…	escutando o ranger da porta você se vira e vê uma pequena forma, segurando uma caixa, se apresenta como Lily, sem apresentar ameaça ela lhe entrega uma caixa de ferramentas, você em choque esfrega os olhos e segura a caixa agradecendo. Lily não se faz presente no gerador, você perplexo apenas começa a consertar, alguns minutos depois escuta pequenos passos vindos da tubulação, você acredita que seja lily, porém é surpreendido por uma queda, uma boneca completamente assombrosa, rapidamente você puxa sua arma e dispara, um dos disparos acertou o gerador, causando chamas. desesperado procura ao redor um extintor, correndo ir pegar, não dando tempo e explodindo a sala, você morre carbonizado junto com a boneca amaldiçoada.""")

class Parte6(Fase):
    
    def executar(self):
        print('''A continuar...
              ''')
        
        return None