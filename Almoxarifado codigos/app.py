from tkinter import Tk
from config import COR_FUNDO, WINDOW_TITLE, WINDOW_SIZE
from tela_login import tela_login
from tela_cadastro import tela_cadastro
from telas_menu import tela_menu
from tela_cadastrar_mercadoria import tela_cadastrar_mercadoria
from tela_inserir_mercadoria import tela_inserir_mercadoria
from tela_consultar_mercadoria import tela_consultar_mercadoria

class App:
    def __init__(self):
        self.dados_cliente = {}
        self.mercadorias = {}

        self.root = Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=COR_FUNDO)

        self.tela_login = tela_login(self)
        self.tela_cadastro = tela_cadastro(self)
        self.tela_menu = tela_menu(self)
        self.tela_cadastrar = tela_cadastrar_mercadoria(self)
        self.tela_inserir = tela_inserir_mercadoria(self)
        self.tela_consultar = tela_consultar_mercadoria(self)

        self.mostrar_tela(self.tela_login.frame)

        self.root.mainloop()

    def mostrar_tela(self, frame):
        """Leva o frame informado para frente (mostra a tela)."""
        frame.tkraise()


if __name__ == "__main__":
    App()