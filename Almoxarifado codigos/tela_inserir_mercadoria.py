from tkinter import Frame, Label, Entry, Button, messagebox
from config import COR_FUNDO, COR_TEXTO, COR_BOTAO, COR_ERRO

class tela_inserir_mercadoria:
    def __init__(self, app):
        self.app = app
        self.frame = Frame(app.root, bg=COR_FUNDO)
        self.frame.grid(row=0, column=0, sticky="nsew")

        Label(self.frame, text="INSERIR MERCADORIA", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)

        Label(self.frame, text="Nome:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
        self.entry_nome = Entry(self.frame)
        self.entry_nome.pack()

        Label(self.frame, text="Quantidade a adicionar:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
        self.entry_qtd = Entry(self.frame)
        self.entry_qtd.pack(pady=5)

        Button(self.frame, text="Adicionar", bg=COR_BOTAO, fg=COR_TEXTO, command=self.inserir).pack(pady=5)
        Button(self.frame, text="Voltar", bg=COR_ERRO, fg=COR_TEXTO, command=lambda: app.mostrar_tela(app.tela_menu.frame)).pack()

    def inserir(self):
        nome = self.entry_nome.get().strip()
        try:
            qtd = int(self.entry_qtd.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida.")
            return

        if not nome:
            messagebox.showwarning("Erro", "Digite um nome válido.")
            return

        if nome not in self.app.mercadorias:
            messagebox.showerror("Erro", "Mercadoria não cadastrada.")
        else:
            self.app.mercadorias[nome]["quantidade"] +- qtd
            messagebox.showinfo("Sucesso", f"{qtd} unidades adicionadas em '{nome}!")
            self.entry_nome.delete(0, "end")
            self.entry_qtd.delete(0, "end")
