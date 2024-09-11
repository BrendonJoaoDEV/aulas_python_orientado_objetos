# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# B) Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver impresso.

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


class Imprimir(Intervalos):
    def __init__(self, inicio, final):
        super().__init__(inicio, final)

    def imprimir_intervalo(self):
        for i in range(self.inicio, self.final + 1):
            print(i, end=', ')
            if i in range(self.inicio, self.final, 20) and i > 1:
                print()


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
            break
        else:
            print('Final inválido! Digite apenas números inteiros!')
    else:
        print('Início inválido! Digite apenas números inteiros!')
print('-'*79)

# Instânciação dos objetos (Processamento de dados):
intervalo = Imprimir(inicio=inicio, final=int(final))

# Saída de dados:
print('.'*79)
print(f'Intervalo de {intervalo.inicio} até {intervalo.final}')
print('.'*79)

intervalo.imprimir_intervalo()
print()

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
