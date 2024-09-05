# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 04/09/2024.
# Autor: Brendon João Campos Neves.
# J) Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

import os


class Calculadora:
    def __init__(self, medida_comprimento, medida_largura):
        self.comprimento = medida_comprimento
        self.largura = medida_largura
    
    def calcular_perimetro(self):
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro
    
