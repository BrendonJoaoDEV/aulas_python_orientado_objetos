# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# B) Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver impresso.

# Importação da biblioteca:
import os


# Definição das classes:
class Intervalos:
    def __init__(self, inicio, final, passo=1):
        self.inicio = int(inicio)
        self.final = int(final)
        self.passo = int(passo)


class Imprimir(Intervalos):
    def imprimir_intervalo(self):
        for i in range(self.inicio, self.final, self.passo):
            print(i, end=', ')
            if i in range(self.inicio, self.final, 20) and i > 1:
                print()

# Declarações de variáveis:
inicio = 0
final = 0
passo = 0
intervalo = object
Impressor = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Imprimir título:
print('.'*79)
print('Imprimir intevalor')
print('.'*79)

# Entrada de dados:
print('-'*79)
while True:
    inicio = input('Digite o início do seu intervalo: ')
    if inicio.isnumeric():
        final = input('Digite o final do seu intervalo: ')
        if final.isnumeric():
            passo = input('Digite o passo do seu intervalo: ')
            if passo == '':
                passo = 1
                break
            elif passo == '0':
                passo = 1
                break
            elif passo.isnumeric():
                break
            else:
                print('Passo inválido! Digite apenas números inteiros!')
        else:
            print('Final inválido! Digite apenas números inteiros!')
    else:
        print('Início inválido! Digite apenas números inteiros!')
print('-'*79)

# Instânciação dos objetos (Processamento de dados):
intervalo = Intervalos(inicio=inicio, final=int(final) + 1, passo=passo)
impressor = Imprimir(intervalo.inicio, intervalo.final, intervalo.passo)

# Saída de dados:
print('.'*79)
print(f'Intervalo de {intervalo.inicio} até {intervalo.final - 1}')
print('.'*79)

impressor.imprimir_intervalo()
print()

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
