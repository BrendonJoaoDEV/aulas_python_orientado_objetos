# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 03/09/2024.
# Autor: Brendon João Campos Neves.
# D) Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

# Importação de bibliotecas:
import os


# Definição da classe:
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dividir(self, a, b):
        quociente = a / b
        return quociente

    def formatar_ponto_flutuante(self, ponto_flutuante, numero_casas):
        formatado = f'{ponto_flutuante: .{numero_casas}f}'
        return formatado


# Declaração de variáveis:
numerador = 0
denominador = 0
quociente = 0
quociente_formatado = 0

# Limpaza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Dividir e formatar números')
print('.'*79)

# Entrada:
print('-'*79)
numerador = float(input('Digite o valor do numerador: '))
denominador = float(input('Digite o valor do denominador: '))
print('-'*79)

# Processamento:
calculador = Calculadora(numerador, denominador)
quociente = calculador.dividir(numerador, denominador)
quociente_formatado = calculador.formatar_ponto_flutuante(quociente, 4)

# Saída:
print('='*79)
print(f'{numerador} / {denominador} = {quociente_formatado}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
