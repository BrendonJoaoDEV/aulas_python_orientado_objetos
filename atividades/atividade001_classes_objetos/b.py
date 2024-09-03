# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 02/09/2024.
# Autor: Brendon João Campos Neves.
# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

# Importação de bibliotecas:
import os


# Criação da classe:
class Usuario:
    def __init__(self, data_nascimento):
        self.data_nascimento = data_nascimento

    def calcular_idade(self, data_nascimento):
        from datetime import datetime

        data_atual = datetime.now()
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        idade = data_atual.year - data_nascimento.year - \
            ((data_atual.month, data_atual.day) <
             (data_nascimento.month, data_nascimento.day))

        return idade


os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Irei descobrir sua idade...')
print('.'*79)

# Entrada
print('-'*79)
data_nascimento = input(
    'Digite a sua data de nascimento (dd/mm/yyyy): ').strip()
print('-'*79)

# Processamento:
pessoa = Usuario(data_nascimento)
idade = pessoa.calcular_idade(data_nascimento)

# Saída:
print('='*79)
print(f'Você tem {idade} anos!')
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
