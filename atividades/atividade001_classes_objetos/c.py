# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 02/09/2024.
# Autor: Brendon João Campos Neves.
# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

import os


class Aluno:
    def __init__(self, nota_1, nota_2, nota_3, nota_4):
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.nota_4 = nota_4

    def media_notas(notas*):
        for nota in notas:
            soma += nota

        media = soma / len(notas)

        return media

print('.'*79)
print('Média de notas')
print('.'*79)