# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# J) Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares,
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

# Importação da biblioteca:
import os


# Definição das classes:
class Intervalos:
    def __init__(self, inicio, final):
        self.inicio = int(inicio)
        self.final = int(final)

    def somar_impares_no_intervalo(self, inicio, final):
        pass


class OperacoesIntervalos(Intervalos):
    def __init__(self, inicio, final):
        super().__init__(inicio, final)

    def somar_impares_no_intervalo(self):
        numero_impares = 0
        soma_impares = 0
        for i in range(self.inicio, self.final + 1):
            if i % 2 != 0:
                numero_impares += 1
                soma_impares += i
        return numero_impares, soma_impares


# Programa principal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Números ímpares de 0 a 100')
print('.'*79)

intervalo = OperacoesIntervalos(0, 100)

print('='*79)
quantidade, soma = intervalo.somar_impares_no_intervalo()
print(f'Soma dos nº ímpares: {soma}')
print(f'Quantidade de nº ímpares encontrados: {quantidade}')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
