from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Titulozinho")
janela.geometry("150x150+200+100")
janela.resizable(FALSE, FALSE)

rotulo = Label(janela, text="Qual é o seu nomezinho?")
rotulo.grid(row=0, column=0)

campo = Entry(janela)
campo.grid(row=1, column=0)

def boasvindas():
    nome = campo.get()
    msg = f"Seja Bem Vindo, {nome}!"
    messagebox.showinfo(message=msg )

botao = Button(janela)
botao.grid(row=2, column=0)
botao["text"] = "Confirmar"
botao["command"] = boasvindas

janela.mainloop()