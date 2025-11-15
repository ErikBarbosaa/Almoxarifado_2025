from tkinter import Frame, Label, Button
from config import COR_FUNDO, COR_TEXTO, COR_BOTAO, COR_ERRO


class tela_menu:
    def __init__(self, app):
        self.app = app
        self.frame = Frame(app.root, bg=COR_FUNDO)
        self.frame.grid(row=0, column=0, sticky="nsew")


        Label(self.frame, text="Menu Principal", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 20, "bold")).pack(pady=20)
        Button(self.frame, text="Consultar Mercadorias", bg=COR_BOTAO, fg=COR_TEXTO, width=25,
               command=lambda: [app.tela_consultar.consultar(), app.mostrar_tela(app.tela_consultar.frame)]).pack(pady=5)
        Button(self.frame, text="Cadastrar Mercadoria", bg=COR_BOTAO, fg=COR_TEXTO, width=25,
               command=lambda: app.mostrar_tela(app.tela_cadastrar.frame)).pack(pady=5)
        Button(self.frame, text="Inserir Mercadorias", bg=COR_BOTAO, fg=COR_TEXTO, width=25,
               command=lambda: app.mostrar_tela(app.tela_inserir.frame)).pack(pady=5)
        Button(self.frame, text="Sair", bg=COR_ERRO, fg=COR_TEXTO, width=25,
               command=lambda: app.mostrar_tela(app.tela_login.frame)).pack(pady=5)