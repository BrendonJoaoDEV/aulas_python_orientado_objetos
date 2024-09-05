# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 04/09/2024.
# Autor: Brendon João Campos Neves.
# H) Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.

# Importação de bibliotecas:
import os


# Definiçã da classe:
class Calculadora:
    def __init__(self, numero):
        self.numero = numero

    def calcular_tabuada(self):
        tabuada = []
        for i in range(1, 11):
            tabuada.append(int(self.numero) * i)

        return tabuada

    def imprimir_tabuada(self, numero, tabuada):
        for multiplicador, resultado in enumerate(tabuada):
            print(f'{numero} x {multiplicador} = {resultado}')


# Declaração de variáveis:
numero = 0
tabuada = []

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Gerar e imprimir tabuada')
print('.'*79)

# Entrada:
print('-'*79)
while True:
    numero = input('Digite o número que deseja a tabuada: ').strip().lower()
    if numero.isnumeric():
        break
    else:
        print('Valor inválido!')
        continue
print('-'*79)

# Processamento:
calculador = Calculadora(numero)
tabuada = calculador.calcular_tabuada()

# Saída:
print('='*79)
calculador.imprimir_tabuada(numero, tabuada)
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
