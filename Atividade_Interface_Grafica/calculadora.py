from tkinter import *

janela = Tk()
janela.title("Calculadora Potente")
janela.geometry("300x150+500+500")
janela.resizable(FALSE, FALSE)

rotulo = Label(janela, text="Valor 1: ")
rotulo.grid(row=0, column=0)

rotulo2 = Label(janela, text="Valor 2: ")
rotulo2.grid(row=1, column=0)

campo1 = Entry(janela)
campo1.grid(row=0, column=1)

campo2 = Entry(janela)
campo2.grid(row=1, column=1)


resultado = Label(janela, text="Resultado:")
resultado.grid(row=5, column=0)

campo3 = Entry(janela)
campo3.grid(row=5, column=1)

def somar():
    v1 = float(campo1.get())
    v2 = float(campo2.get())
    r = f"{v1 + v2}"
    campo3.config(state=NORMAL)
    campo3.delete(0, END)
    campo3.insert(0, r)
    campo3.config(state=DISABLED)

def subtrair():
    v1 = float(campo1.get())
    v2 = float(campo2.get())
    r = f"{v1 - v2}"
    campo3.config(state=NORMAL)
    campo3.delete(0, END)
    campo3.insert(0, r)
    campo3.config(state=DISABLED)

def multiplicar():
    v1 = float(campo1.get())
    v2 = float(campo2.get())
    r = f"{v1 * v2}"
    campo3.config(state=NORMAL)
    campo3.delete(0, END)
    campo3.insert(0, r)
    campo3.config(state=DISABLED)

def dividir():
    v1 = float(campo1.get())
    v2 = float(campo2.get())
    r = f"{v1 / v2}"
    campo3.config(state=NORMAL)
    campo3.delete(0, END)
    campo3.insert(0, r)
    campo3.config(state=DISABLED)

    
botao1 = Button(janela, text="Somar", bg="pink", width="9")
botao1.grid(row=2, column=1)
botao1["command"] = somar

botao2 = Button(janela, text="Subtrair", bg="orchid2", width="9")
botao2.grid(row=2, column=2)
botao2["command"] = subtrair

botao3 = Button(janela, text="Multiplicar", bg="cyan", width="9")
botao3.grid(row=3, column=1)
botao3["command"] = multiplicar

botao4 = Button(janela, text="Dividir", bg="sky blue", width="9")
botao4.grid(row=3, column=2)
botao4["command"] = dividir

janela.mainloop()