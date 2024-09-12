# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# F) Faça um programa que imprima os números primos entre 0 e 100.

# Importação da biblioteca:
import os


# Definição da classe:
class Intervalos:
    def __init__(self, inicio, final, passo=1):
        self.inicio = int(inicio)
        self.final = int(final)
        self.passo = int(passo)


class OperacoesIntervalos(Intervalos):
    def verificar_primo(self):
        for i in range(self.inicio, self.final + 1):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    print(i, end=', ')
                    if i in range(self.inicio, self.final + 1, 73):
                        print()


# Declarações de variáveis:
intervalo = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Intânciação do objeto:
intervalo = OperacoesIntervalos(0, 100 + 1)

# Imprimindo título:
print('.'*79)
print('Números primos no intervalo de 0 a 100')
print('.'*79)

# Imprimindo os primos:
print('='*79)
intervalo.verificar_primo()
print()
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
