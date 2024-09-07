# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# B) Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver impresso.

# Importação da biblioteca:
import os


# Definição da classe:
class Intervalos:
    def __init__(self, inicio, final, passo=1):
        self.inicio = int(inicio)
        self.final = int(final) 
        self.passo = int(passo)

    def imprimir_intervalo(self):
        for i in range(self.inicio, self.final, self.passo):
            print(i, end=', ')


# Declarações de variáveis:
inicio = 0
final = 0
passo = 0
intervalo = object

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

# Instânciação do objeto (Processamento de dados):
intervalo = Intervalos(inicio=inicio, final=final + 1, passo=passo)

# Saída de dados:
print('.'*79)
print(f'Intervalo de {intervalo.inicio} até {intervalo.final - 1}')
print('.'*79)

intervalo.imprimir_intervalo()
print()

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
