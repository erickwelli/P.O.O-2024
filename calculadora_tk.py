from tkinter import *

cor1 = '#1e1f1e' #preto
cor2 = '#feffff' #branco
cor3 = '#38576b' #azul
cor4 = '#eceff1' #cinza
cor5 = '#ffab40' #laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ''
#criando função
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    #resultado = eval('9/9')
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    #print(resultado)

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

valor_texto = StringVar()

#criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#criando os botões
b_1 = Button(frame_corpo, text='C',command=lambda: limpar_tela(), width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text='%',command=lambda: entrar_valores('%'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, text='/',command=lambda: entrar_valores('/'), width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text='7',command=lambda: entrar_valores('7'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, text='8',command=lambda: entrar_valores('8'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo, text='9',command=lambda: entrar_valores('9'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, text='*',command=lambda: entrar_valores('*'), width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, text='4',command=lambda: entrar_valores('4'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo, text='5',command=lambda: entrar_valores('5'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_corpo, text='6',command=lambda: entrar_valores('6'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_corpo, text='-',command=lambda: entrar_valores('-'), width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, text='1',command=lambda: entrar_valores('1'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, text='2',command=lambda: entrar_valores('2'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo, text='3',command=lambda: entrar_valores('3'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo, text='+',command=lambda: entrar_valores('+'), width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, text='0',command=lambda: entrar_valores('0'), width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_18 = Button(frame_corpo, text='.',command=lambda: entrar_valores('.'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=118, y=208)

b_19 = Button(frame_corpo, text='=',command=lambda: calcular(), width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_19.place(x=177, y=208)

# entrar_valores()
janela.mainloop()