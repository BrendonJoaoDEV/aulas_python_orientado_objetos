# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 11/09/2024.
# Autor: Brendon João Campos Neves.
# G) Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

# importação da biblioteca:
import os


# definição da classe:
class Intervalos:
    def __init__(self, inicio, final):
        self.inicio = int(inicio)
        self.final = int(final)

    def verificar_primo(self, inicio, final):
        # Método que será sobrecarregado
        pass


class OperacoesIntervalos(Intervalos):
    def __init__(self, inicio, final):
        super().__init__(inicio, final)

    def verificar_primo(self):
        for i in range(self.inicio, self.final):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    print(i, end=', ')
                    if i in range(self.inicio, self.final, 73):
                        print()


# Declarações de variáveis:
inicio = 0
final = 0
passo = 0
intervalo = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Encontrar números primos')
print('.'*79)

# Entrada:
print('-'*79)
while True:
    inicio = input('Digite o início do seu intervalo: ')
    if inicio.isnumeric():
        final = input('Digite o final do seu intervalo: ')
        if final.isnumeric():
            break
        else:
            print('Final inválido! Digite apenas números inteiros!')
    else:
        print('Início inválido! Digite apenas números inteiros!')
print('-'*79)

# Processamento:
intervalo = OperacoesIntervalos(inicio, final)

# Saída:
print('='*79)
intervalo.verificar_primo()
print()
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
