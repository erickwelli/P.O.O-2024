from tkinter import *
import tkinter
from datetime import *

#cores
cor1 = '#3d3d3d' #preta
cor2 = '#fafcff' #branco
cor3 = '#21c25c' #verde
cor4 = '#H50914' #vermelho
cor5 = '#dedcdc' #cinza
cor6 = '#3080f0' #azul


janela = Tk()
janela.title('Relógio Digital')
janela.geometry("440x180")
janela.resizable(width=FALSE, height=False)
janela.configure(bg=cor1)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.strftime("%d")
    mes = tempo.strftime("%b") #B = Janeiro / b = Jan
    ano = tempo.strftime("%Y")
    l1.config(text=hora)
    l1.after(100, relogio)
    l2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, font=("Arial, 80"), bg= cor1, fg=cor5)
l1.grid(row=0, column=0, sticky=NW, padx=5)


l2 = Label(janela, font=("Arial, 20"), bg= cor1, fg=cor5)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()

janela.mainloop()