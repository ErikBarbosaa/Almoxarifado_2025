from tkinter import Frame, Label, Entry, Button, messagebox
from config import COR_FUNDO, COR_TEXTO, COR_BOTAO, COR_ERRO


class tela_cadastro:
    def __init__(self, app):
        self.app = app
        self.frame = Frame(app.root, bg=COR_FUNDO)
        self.frame.grid(row=0, column=0, sticky="nsew")

        Label(self.frame, text="Cadastro", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 20, "bold")).pack(pady=20)
        Label(self.frame, text="Usuario:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
        self.entry_user = Entry(self.frame)
        self.entry_user.pack()


        Label(self.frame, text="Senha:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
        self.entry_senha = Entry(self.frame, show="*")
        self.entry_senha.pack()

        Label(self.frame, text="Repita a senha:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
        self.entry_resenha = Entry(self.frame, show="*")
        self.entry_resenha.pack(pady=5)


        Button(self.frame, text="Cadastrar", bg=COR_BOTAO, fg=COR_TEXTO, command=self.cadastrar).pack(pady=5)
        Button(self.frame, text="Voltar", bg=COR_ERRO, fg=COR_TEXTO, command=lambda: app.mostrar_tela(app.tela_login.frame)).pack()


    def cadastrar(self):
        user = self.entry_user.get().strip()
        senha = self.entry_senha.get().strip()
        resenha = self.entry_resenha.get().strip()


        if user in self.app.dados_cliente:
            messagebox.showerror("Erro", "Usuario já Existe.")
        elif senha != resenha:
            messagebox.showerror("Erro", "As senhas não coincidem")
        elif not user or not senha:
            messagebox.showwarning("Erro", "Preencha todos os campos.")
        else:
            self.app.dados_cliente[user] = {"senha": senha}
            messagebox.showinfo("Sucesso", "Usuário cadastrado com succeso!")
            self.entry_user.delete(0, "end")
            self.entry_senha.delete(0, "end")
            self.entry_resenha.delete(0, "end")
            self.app.mostrar_tela(self.app.tela_login.frame)
