# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# D) Faça um programa que imprima os números pares entre 0 e 100.

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
intervalo = object
impressor = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Intânciação dos objetos:
intervalo = Intervalos(inicio=0, final=100 + 1, passo=2)
impressor = Imprimir(intervalo.inicio, intervalo.final, intervalo.passo)

# Imprimindo título:
print('.'*79)
print('Intervalo com os números pares de 0 a 100')
print('.'*79)

# Imprimindo o intervalo:
impressor.imprimir_intervalo()
print()

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
