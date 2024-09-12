# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# I) Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

# Importação da biblioteca:
import os


# Definição da classe:
class Jogo:
    def looping(self, resposta):
        pass


class JogoLooping(Jogo):
    def looping(self):
        resposta = ''
        while resposta != 'f':
            print('.'*79)
            print('Estou em looping!')
            print('.'*79)
            print('-'*79)
            resposta = str(input(
                'Digite uma letra para salvar o sistema: ')).strip().lower()
        print('-'*79)


# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

jogador = JogoLooping()
jogador.looping()

print('='*79)
print('Fim do jogo! Obrigado por jogar ;)')
print('='*79)
