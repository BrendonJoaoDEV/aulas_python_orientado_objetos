# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# L) Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

# Importação da biblioteca:
import os


# Definição das classes:
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def logar(self, nome, senha):
        pass


class Cadastrado(Usuario):
    def __init__(self, nome, senha):
        super().__init__(nome, senha)

    def logar(self, usuario):
        while True:
            nome = str(input('Digite seu nome: ')).strip()
            senha = str(input('Digite sua senha: ')).strip()
            confirmacao = str(input('Digite sua senha novamente: ')).strip()
            if senha == confirmacao:
                if nome == usuario.nome and senha == usuario.senha:
                    break
                else:
                    print('Credenciais incorretas!')
            else:
                print('Sua senha e confirmação são diferentes!')


# Programa principal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Bem vindo novo usuário!')
print('.'*79)

print('-'*79)
while True:
    nome = str(input('Digite seu nome: ')).strip()
    senha = str(input('Digite sua senha: ')).strip()
    confirmacao = str(input('Digite sua senha novamente: ')).strip()
    if senha == confirmacao:
        usuario = Cadastrado(nome, senha)
        break
    else:
        print('Sua senha e confirmação são diferentes!')
print('-'*79)

print('~'*79)

print('.'*79)
print('Logar usuário')
print('.'*79)

print('-'*79)
usuario.logar(usuario)
print('-'*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
