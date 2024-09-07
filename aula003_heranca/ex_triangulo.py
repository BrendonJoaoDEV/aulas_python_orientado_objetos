# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 05/09/2024.

import os
import math


class Triangulo:
    def __init__(self, cateta_1, cateto_2):
        self.cateta_1 = cateta_1
        self.cateto_2 = cateto_2


class TrianguloRetangulo(Triangulo): # Herança
    def calcular_hipotenusa(self):
        resultado = math.sqrt(pow(self.cateta_1, 2)) + pow(self.cateto_2, 2)
        return resultado


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    cateto_1 = float(input('Entre com o cateto a: '))
    cateto_2 = float(input('Entre com o cateto b: '))
    
    if cateto_1 == 0 or cateto_2 == 0:
        print('Fim do programa!')
        break
    else:
        triangulo_retangulo = TrianguloRetangulo(cateto_1, cateto_2)
        hipotenusa = triangulo_retangulo.calcular_hipotenusa()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f'O triângulo retângulo de lado 1 = {cateto_1} e')
        print(f'
              de lado 2 = {cateto_2} é igual a {hipotenusa: .2f} aproximadamente!')
        input('Pressione ENter para retornar...')