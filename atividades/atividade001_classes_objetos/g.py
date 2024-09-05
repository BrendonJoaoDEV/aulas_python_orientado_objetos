# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 03/09/2024.
# Autor: Brendon João Campos Neves.
# G) Faça um programa que converta metros em centímetros e milímetros.

# Importação da biblioteca:
import os


# Definição da classe:
class Convercao:
    def __init__(self, medida, unidade):
        self.medida = medida
        self.unidade = unidade

    def converter_unidade(self, medida, unidade_atual='m', unidade_final='cm'):
        if unidade_atual == 'm' and unidade_final == 'cm':
            medida_convertido = medida * 100
            medida_convertido = str(medida_convertido) + unidade_final
        elif unidade_atual == 'm' and unidade_final == 'mm':
            medida_convertido = medida * 1000
            medida_convertido = str(medida_convertido) + unidade_final
        elif unidade_atual == 'cm' and unidade_final == 'm':
            medida_convertido = medida / 100
            medida_convertido = str(medida_convertido) + unidade_final
        elif unidade_atual == 'cm' and unidade_final == 'mm':
            medida_convertido = medida * 10
            medida_convertido = str(medida_convertido) + unidade_final
        elif unidade_atual == 'mm' and unidade_final == 'm':
            medida_convertido = medida / 1000
            medida_convertido = str(medida_convertido) + unidade_final
        elif unidade_atual == 'mm' and unidade_final == 'cm':
            medida_convertido = medida / 10
            medida_convertido = str(medida_convertido) + unidade_final
        else:
            medida_convertido = 'Unidades não suportadas!'

        return medida_convertido


# Declarações de variáveis:
medida = 0
unidade_atual = ''
unidade_final = ''
medida_convertida = 0

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Converção de unidade:')
print('m > cm > mm')
print('m < cm < mm')
print('.'*79)

# Entrada:
print('-'*79)
while True:
    try:
        medida = float(input('Digite a medida sem a unidade: '))
        unidade_atual = str(
            input('Digite a unidade (m/cm/mm): ')).strip().lower()
        unidade_final = str(input(
            'Digite a unidade que deseja obter a medida: ')).strip().lower()
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        break
print('-'*79)

# Processamento:
conversor = Convercao(medida, unidade_atual)
medida_convertida = conversor.converter_unidade(
    medida, unidade_atual=unidade_atual, unidade_final=unidade_final)

# Saída:
print('='*79)
print(f'{medida}{unidade_atual} para {unidade_final} = {medida_convertida}')
print('='*79)

print('.'*79)
print('FIm do programa! Obrigado ;)')
print('.'*79)
