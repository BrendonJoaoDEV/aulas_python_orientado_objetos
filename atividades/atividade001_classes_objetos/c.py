# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 02/09/2024.
# Autor: Brendon João Campos Neves.
# C) Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

# Importação de bibliotecas:
import os


# Denifição da classe:
class Aluno:
    def __init__(self, nota_1=0, nota_2=0, nota_3=0, nota_4=0):
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.nota_4 = nota_4

    def pedir_notas(self):
        notas = []
        for i in range(1, 5):
            notas.append(float(input(f'Digite sua {i}º nota: ')))

        self.nota_1 = notas[0]
        self.nota_2 = notas[1]
        self.nota_3 = notas[2]
        self.nota_4 = notas[3]

        return notas

    def exibir_notas(self, notas):
        c = 0
        for nota in notas:
            c += 1
            print(f'{c}º nota: {nota: .2f}')

    def calcular_media_notas(self, notas):
        soma = 0
        for nota in notas:
            soma += nota

        media = soma / len(notas)

        return media


# Declaração de variáveis:
notas = []
media_notas = 0

# Criação do objeto:
novo_aluno = Aluno()

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Média de notas')
print('.'*79)

# Entrada:
print('-'*79)
notas = novo_aluno.pedir_notas()
print('-'*79)

# Processamento:
media_notas = novo_aluno.calcular_media_notas(notas)

# Saída:
print('='*79)
novo_aluno.exibir_notas(notas)
print(f'Média das notas do aluno: {media_notas}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
