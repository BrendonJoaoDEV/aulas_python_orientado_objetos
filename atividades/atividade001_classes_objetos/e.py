# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 03/09/2024.
# Autor: Brendon João Campos Neves.
# E) Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

# Importação de bibliotecas:
import os


# Definição da classe:
class Numeros():
    def __init__(self, numero):
        self.numero = numero

    def calcular_antecessor(self, numero):
        antecessor = numero - 1
        return antecessor

    def calcular_sucessor(self, numero):
        sucessor = numero + 1
        return sucessor


# Declaração de variáveis:
numero = 0
antecessor = 0
sucessor = 0

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Calcular antecessor e sucessor')
print('.'*79)

# Entrada:
print('-'*79)
while True:
    numero = input('Digite um número: ')
    if numero.isnumeric():
        numero = int(numero)
        break
    else:
        print('Entrada inválida!')
print('-'*79)

# Processamento:
gerenciador_numeros = Numeros(numero)
antecessor = gerenciador_numeros.calcular_antecessor(numero)
sucessor = gerenciador_numeros.calcular_sucessor(numero)

# Saída:
print('='*79)
print(f'Número: {numero}')
print(f'Antecessor: {antecessor}')
print(f'Sucessor: {sucessor}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
