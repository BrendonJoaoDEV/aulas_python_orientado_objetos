# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 04/09/2024.
# Autor: Brendon João Campos Neves.
# I) Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.

# Importação das bibliotecas:
import os


# Definição da classe:
class Convercao():
    def __init__(self, valor_em_reais):
        self.valor_em_reais = valor_em_reais
        self.valor_em_dolares = 0

    def converter_reais_dolares(self, valor_em_reais):
        valor_em_dolares = float(valor_em_reais) / 5.64
        self.valor_em_dolares = valor_em_dolares
        return valor_em_dolares


# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Converter valor em reais para dólares')
print('.'*79)

# Entrada:
print('-'*79)
while True:
    valor_em_reais = input('Digite um valor em reais: ').strip().lower()
    if valor_em_reais.replace('.', '').isnumeric():
        break
    else:
        print('Valor inválido!')
    continue
print('-'*79)

# Processamento:
conversor = Convercao(valor_em_reais)
valor_em_dolares = conversor.converter_reais_dolares(valor_em_reais)

# Saída:
print('='*79)
print(f'{valor_em_reais}R$ em dólares é {valor_em_dolares}$')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
