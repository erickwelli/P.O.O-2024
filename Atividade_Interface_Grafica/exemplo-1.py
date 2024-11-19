from tkinter import *


janela = Tk()
rotulo = Label(janela, text="Hello, word! \nI am testing Tkinter!", pady=5, padx= 10)
rotulo.grid(row=0, column=0)
rotulo["font"] = ("Arial", "15", "bold", "italic")
rotulo["fg"] = "white"  
rotulo["bg"] = "black"
rotulo["underline"] = 0
rotulo["height"] = 4


rotulo2 = Label(janela, text="I love sport bikes! \nThey are beautiful!", pady=5, padx= 10)
rotulo2.grid(row=1, column=0)
rotulo2["font"] = ("Arial", "15", "bold", "italic")
rotulo2["bg"] = "white"
rotulo2["height"] = 4

info = """Look how interesting!
The H2R motorcycle is the fastest in the world!
And very beautiful!
"""

rotulo3 = Label(janela, text = info, justify= "left", padx=10, pady=5)
rotulo3.grid(row=0, column=2)   
rotulo3["font"] = ("Arial", "15", "bold", "italic")
rotulo3["fg"] = "white"  
rotulo3["bg"] = "black"
rotulo2["height"] = 4

imagembike = PhotoImage(file="D:/Users/20231041110005/Documents/POO/P.O.O-2024/Atividade_Interface_Grafica/imagens/bike.png")

rotulo4 = Label(janela, text= info, image=imagembike)
rotulo4.grid(row=0, column=1)
rotulo4["width"] = 450
rotulo4["height"] = 450


botao_sair = Button(janela, padx=25, pady=5, justify="center")
botao_sair.grid(row=1, column=2)
botao_sair["text"] = "Sair"
botao_sair["width"] = 5
botao_sair["command"] = quit
botao_sair["bd"] = 5
botao_sair["bg"] = "red"
botao_sair["activebackground"] = "pink"
botao_sair["fg"] = "white"
botao_sair["font"] = ("Arial", "10", "bold", "italic")

janela.mainloop()