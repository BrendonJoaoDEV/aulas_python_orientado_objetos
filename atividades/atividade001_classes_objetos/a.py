# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 02/09/2024.
# Autor: Brendon João Campos Neves.
# A) Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores.

# Importação de bibliotecas:
import os


# Criação da classe:
class Calculadora:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def somar(self, a, b, c):
        soma = a + b + c
        return soma

    def subtrair(self, a, b, c):
        diferenca = a - b - c
        return diferenca

    def multiplicar(self, a, b, c):
        produto = a * b * c
        return produto


# Declarações de variáveis:
a = 0
b = 0
c = 0
soma = 0
diferenca = 0
produto = 0
escolha = ''

# Sistema:
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('.'*79)
    print('Calculadora')
    print('.'*79)

    # Entrada:
    print('-'*79)
    a = int(input('Digite seu 1º valor: '))
    b = int(input('Digite seu 2º valor: '))
    c = int(input('Digite seu 3º valor: '))
    print('-'*79)

    # Processamento:
    calculador = Calculadora(a, b, c)
    soma = calculador.somar(a, b, c)
    diferenca = calculador.subtrair(a, b, c)
    produto = calculador.multiplicar(a, b, c)

    # Saída:
    print('='*79)
    print(f'{a} + {b} + {c} = {soma}')
    print(f'{a} - {b} - {c} = {diferenca}')
    print(f'{a} x {b} x {c} = {produto}')
    print('='*79)

    escolha = input('Deseja fazer outros cálculos (s/n): ').strip().lower()
    if escolha == 's':
        continue
    else:
        break
