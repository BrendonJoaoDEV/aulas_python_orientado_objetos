# curso de desenvolvimento de sistemas.
# turma: 0152.
# data: 09/09/2024.
# autor: brendon joão campos neves.
# g) faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

# importação da biblioteca:
import os


# definição da classe:
class intervalos:
    def __init__(self, inicio, final, passo=1):
        self.inicio = int(inicio)
        self.final = int(final)
        self.passo = int(passo)


class operacoesintervalos(intervalos):
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
operario = object

print('.'*79)
print('Encontrar números primos')
print('.'*79)