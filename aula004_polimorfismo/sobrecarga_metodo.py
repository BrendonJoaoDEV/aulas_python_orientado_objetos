# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 11/09/2024.
# Sobrecarga de Métodos:

class ClassePai: # Super Classe
    # Método Construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Para sobrecarregar
    # Vai ser usado para somar 2 números
    def metodo_classe(self, a, b):
        pass


class ClasseFilha: # Classe Derivada
    # Método Construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Sobrecarga de Método
    def metodo_classe(self):
        return self.a + self.b

# Programa Principal
teste = ClasseFilha(1,2)
teste.metodo_classe()