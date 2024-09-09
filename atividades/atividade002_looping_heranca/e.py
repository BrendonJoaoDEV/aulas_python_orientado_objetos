# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# E) Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

# Importação da biblioteca:
import os


# Definição das classes:
class Intervalos:
    def __init__(self, inicio, final, passo=1):
        self.inicio = int(inicio)
        self.final = int(final)
        self.passo = int(passo)


class OperacoesIntervalos(Intervalos):
    def somar_pares_no_intervalo(self):
        numero_pares = 0
        soma_pares = 0
        for i in range(self.inicio, self.final, self.passo):
            if i % 2 == 0:
                numero_pares += 1
                soma_pares += i
        return numero_pares, soma_pares


# Declarações de variáveis:
intervalo = object
operario = object
numero_pares = 0
soma_pares = 0

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Instânciação dos objetos:
intervalo = Intervalos(0, 100 + 1)
operario = OperacoesIntervalos(intervalo.inicio, intervalo.final, intervalo.passo)
# Imprimindo título:
print('.'*79)
print('Número de pares e soma de todos os pares no intervalo de 0 a 100')
print('.'*79)

# Processamento de dados:
numero_pares, soma_pares = operario.somar_pares_no_intervalo()

# Saída de daddos:
print('='*79)
print(f'O número de números pares no intervalo é {numero_pares}')
print(f'A soma desses números pares é: {soma_pares}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
