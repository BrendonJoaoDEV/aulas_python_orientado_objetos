# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 04/09/2024.
# Autor: Brendon João Campos Neves.
# J) Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

# Importação das bibliotecas:
import os


# Definição da classe:
class Calculadora:
    def __init__(self, medida_comprimento, medida_largura):
        self.comprimento = medida_comprimento
        self.largura = medida_largura
    
    def calcular_perimetro(self):
        perimetro = (int(self.comprimento) * 2) + (int(self.largura) * 2)
        return perimetro
    

# Declarações de variáveis:
comprimento = 0.0
largura = 0.0
perimetro = 0.0

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Calcular perímetro de um retângulo')
print('.'*79)

# Entrada:
print('-'*79)
while True:
    comprimento = input('Digite o comprimento da base do seu retângulo: ')
    if comprimento.replace('.', '').isnumeric():
        largura = input('Digite a largura do lado do seu retângulo: ')
        if largura.replace('.', '').isnumeric():
            break
        else:
            print('Largura inválida!')
    else:
        print('Comprimento inválida!')
print('-'*79)

# Processamento:
calculador = Calculadora(comprimento, largura)
perimetro = calculador.calcular_perimetro()

# Saída:
print('='*79)
print(f'O perímetro do retângulo é {perimetro}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)