# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# D) Faça um programa que imprima os números pares entre 0 e 100.

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
        self.inicio = int(inicio)
        self.final = int(final)

    def imprimir_intervalo(self):
        for i in range(self.inicio, self.final + 1):
            if i % 2 == 0:
                print(i, end=', ')
            if i in range(self.inicio, self.final, 20) and i > 1:
                print()


# Declarações de variáveis:
intervalo = object
impressor = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Intânciação dos objetos:
intervalo = Intervalos(0, 100)
impressor = Imprimir(intervalo.inicio, intervalo.final)

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
