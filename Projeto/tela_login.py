from tkinter import Frame, Label, Entry, Button, messagebox
from config import COR_FUNDO, COR_TEXTO, COR_BOTAO


class tela_login:
    def __init__(self, app):
        self.app = app
        self.frame = Frame(app.root, bg=COR_FUNDO)
        self.frame.grid(row=0, column=0, sticky="nsew")


        Label(self.frame, text="LOGIN", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 20, "bold")).pack(pady=20)
        Label(self.frame, text="Usuário:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
        self.entry_user = Entry(self.frame)
        self.entry_user.pack()


        Label(self.frame, text="Senha:", bg=COR_FUNDO, fg=COR_TEXTO).pack()
        self.entry_senha = Entry(self.frame, show="*")
        self.entry_senha.pack(pady=5)

        Button(self.frame, text="Entrar", bg=COR_BOTAO, fg=COR_TEXTO, command=self.login).pack(pady=5)
        Button(self.frame,text="Cadastrar", bg=COR_BOTAO, fg=COR_TEXTO, command=lambda: app.mostrar_tela(app.tela_cadastro.frame)).pack()

    
    def login(self):
        user = self.entry_user.get().strip()
        senha = self.entry_senha.get().strip()


        if user in self.app.dados_cliente and self.app.dados_cliente[user]["senha"] == senha:
            messagebox.showinfo("Sucesso", f"Bem-Vindo, {user}!")
            self.app.mostrar_tela(self.app.tela_menu.frame)

            self.entry_user.delete(0, "end")
            self.entry_senha.delete(0, "end")
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")