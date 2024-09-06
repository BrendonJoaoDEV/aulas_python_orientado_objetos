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