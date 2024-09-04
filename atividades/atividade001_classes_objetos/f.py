# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 03/09/2024.
# Autor: Brendon João Campos Neves.
# F) Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

# Importação de bibliotecas:
import os


# Declaração da classe:
class Calculadora:
    def __init__(self, numero):
        self.numero = numero

    def dobrar(self, numero):
        dobro = numero * 2
        return dobro

    def triplicar(self, numero):
        triplo = numero * 3
        return triplo


# Declaração de variáveis:
numero = 0
dobro = 0
triplo = 0

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Calcular: dobro e triplo')
print('.'*79)

print('-'*79)
while True:
    numero = input('Digite um número: ')
    if numero.isnumeric():
        numero = int(numero)
        break
    else:
        print('Entrada inválida!')
print('-'*79)

calculador = Calculadora(numero)
dobro = calculador.dobrar(numero)
triplo = calculador.triplicar(numero)

print('='*79)
print(f'Número: {numero}')
print(f'Dobro: {dobro}')
print(f'Triplo: {triplo}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
