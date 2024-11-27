from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Bloquinho de Login")
janela.resizable(FALSE, FALSE)
janela.geometry("250x250+300+500")

usuario = Label(janela, text="Usuário: ")
usuario.grid(row=0, column=0, padx=10, pady=10)

campo_usuario = Entry(janela)
campo_usuario.grid(row=0, column=1, padx=10, pady=10)

senha = Label(janela, text="Senha: ")
senha.grid(row=1, column=0, padx=10, pady=10)

campo_senha = Entry(janela, show="*")
campo_senha.grid(row=1, column=1, padx=10, pady=10)

def verificar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "erickigarshi" and senha == "lobinhoazul":
        messagebox.showinfo(message="Login feito com sucesso!")

    else:
        messagebox.showinfo(message="Login negado! Tente novamente.")

botao = Button(janela, text="Entrar", command=verificar_login)
botao.grid(row=2, columnspan=2, pady=20)

janela.mainloop()