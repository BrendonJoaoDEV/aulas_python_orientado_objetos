# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 03/09/2024.
# Autor: Brendon João Campos Neves.
# G) Faça um programa que converta metros em centímetros e milímetros.

import os

class Convercao:
    def __init__(self, medida, unidade):
        self.medida = medida
        self.unidade = unidade
        
    def converter_unidade(self, medida, unidade_atual='m', unidade_final='cm'):
        if unidade_atual == 'm' and unidade_final == 'cm':
            valor_convertido = medida * 100
            valor_convertido = str(valor_convertido) + unidade_final
        elif unidade_atual == 'm' and unidade_final == 'mm':
            valor_convertido = valor * 1000
            valor_convertido = str(valor_convertido) + unidade_final
        elif unidade_atual == 'cm' and unidade_final == 'm':
            valor_convertido = valor / 100
            valor_convertido = str(valor_convertido) + unidade_final
        elif unidade_atual == 'cm' and unidade_final == 'mm':
            valor_convertido = valor * 10
            valor_convertido = str(valor_convertido) + unidade_final
        elif unidade_atual == 'mm' and unidade_final == 'm':
            valor_convertido = valor / 1000
            valor_convertido = str(valor_convertido) + unidade_final
        elif unidade_atual == 'mm' and unidade_final == 'cm':
            valor_convertido = valor / 10
            valor_convertido = str(valor_convertido) + unidade_final
        else:
            valor_convertido = 'Unidades não suportadas!'


os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Converção de unidade:')
print('m > cm > mm')
print('m < cm < mm')
print('.'*79)

print('-'*79)
while True:
    try:
        medida = float(input('Digite a medida sem a unidade: '))
        unidade = str(input('Digite a unidade (m/cm/mm): '))
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        break
print('-'*79)

conversor = Convercao(valor, unidade)
mediaconversor