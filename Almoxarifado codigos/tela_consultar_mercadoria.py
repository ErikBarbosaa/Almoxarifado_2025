from tkinter import Frame, Label, Text, Button
from config import COR_FUNDO, COR_TEXTO, COR_BOTAO, COR_ERRO

class tela_consultar_mercadoria:
    def __init__(self, app):
        self.app = app
        self.frame = Frame(app.root, bg=COR_FUNDO)
        self.frame.grid(row=0, column=0, sticky="nsew")

        Label(self.frame, text="CONSULTAR MERCADORIAS", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)
        self.texto = Text(self.frame, width=50, height=10)
        self.texto.pack()

        Button(self.frame, text="Atualizar", bg=COR_BOTAO, fg=COR_TEXTO, command=self.consultar).pack(pady=5)
        Button(self.frame, text="Voltar", bg=COR_ERRO, fg=COR_TEXTO, command=lambda: app.mostrar_tela(app.tela_menu.frame)).pack()

    def consultar(self):
        self.texto.delete(1.0, "end")
        if not self.app.mercadorias:
            self.texto.insert("end", "Nenhuma mercadoria cadastrada.\n")
        else:
            for nome, info in self.app.mercadorias.items():
                self.texto.insert("end", f"{nome}: {info['quantidade']} unidades - R${info['preço']:2f}\n")
                