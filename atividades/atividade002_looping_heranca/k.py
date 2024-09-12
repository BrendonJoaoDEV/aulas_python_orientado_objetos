# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# K) Crie um programa que pede que o usuário digite um nome ou uma frase, 
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

# Importação da biblioteca:
import os


# Definição da classe:
class Frase:
    def __init__(self, cadeia_caracteres):
        self.frase = cadeia_caracteres
    
    def verificar_palindormo(self, cadeia_caracteres):
        # Método que será sobrecarregado.
        pass


class Palindromo(Frase):
    def __init__(self, cadeia_caracteres):
        super().__init__(cadeia_caracteres)
    
    def verificar_palindormo(self):
        frase = str(self.frase).replace(' ', '').lower()
        frase_invertida = frase[::-1]
        if frase == frase_invertida:
            print(f'{self.frase} é um palímdromo!')
        else:
            print(f'{self.frase} não é um palíndromo!')


# Programa Principal:
os.system('cls' if os.name == 'nt' else 'clear')

print('.'*79)
print('Verificar se frases são palídromos')
print('.'*79)

# Entrada:
print('-'*79)
frase = str(input('Digite sua palavra ou frase: ')).strip()
print('-'*79)

# Processamento:
escritor = Palindromo(frase)

# Saída:
print('='*79)
escritor.verificar_palindormo()
print('='*79)

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)