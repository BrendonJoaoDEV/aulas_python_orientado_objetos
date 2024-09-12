# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 12/09/2024.
# Autor: Brendon João Campos Neves.
# H) Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

# Importação da biblioteca:
import os


# Definição das classes:
class Intervalos:
    def __init__(self, inicio, final):
        self.inicio = int(inicio)
        self.final = int(final)

    def imprimir_intervalo(self, inicio, final):
        # Método que será sobrecarregado.
        pass


class Excluidos(Intervalos):
    def __init__(self, inicio, final, excluido_1, excluido_2, excluido_3):
        super().__init__(inicio, final)
        self.excluido_1 = excluido_1
        self.excluido_2 = excluido_2
        self.excluido_3 = excluido_3

    def imprimir_intervalo(self):
        for i in range(self.inicio, self.final + 1):
            if (i == self.excluido_1 or i == self.excluido_2
                    or i == self.excluido_3):
                continue
            else:
                print(i, end=', ')
                if i in range(self.inicio, self.final, 20) and i > 1:
                    print()


# Declarações de variáveis:
inicio = 0
final = 0
excluido_1 = 0
excluido_2 = 0
excluido_3 = 0
intervalo = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Imprimir título:
print('.'*79)
print('Imprimir intevalor excluindo três números')
print('.'*79)

# Entrada de dados:
print('-'*79)
while True:
    try:
        inicio = int(input('Digite o início do seu intervalo: '))
        final = int(input('Digite o final do seu intervalo: '))
        excluido_1 = int(input('Digite o 1º valor que deseja excluir: '))
        excluido_2 = int(input('Digite o 2º valor que deseja excluir: '))
        excluido_3 = int(input('Digite o 3º valor que deseja excluir: '))
    except ValueError:
        print('Algum dos valores inseridos é inválido! Digite apenas números inteiros!')
    else:
        break
print('-'*79)

# Instânciação dos objetos (Processamento de dados):
intervalo = Excluidos(inicio, final, excluido_1, excluido_2, excluido_3)

# Saída de dados:
print('.'*79)
print(f'Intervalo de {intervalo.inicio} até {intervalo.final}')
print('.'*79)

print('='*79)
intervalo.imprimir_intervalo()
print()
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
