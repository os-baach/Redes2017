# Calculadora con más operaciones
from .Calculator import Calculator

class ScientificCalculator(Calculator):

    # Multiplica n1 x n2
    def multiplica(self, n1, n2):
        return n1 * n2

    # Divide n1 / n2
    def divide(self, n1, n2):
        if n2 == 0:
            return float('nan')
        return float(n1/n2)

    # Regresa n1 % n2
    def modulo(self, n1, n2):
        if n2 == 0:
            return float('nan')
        return n1 % n2

    # Regresa n1 ^ n2
    def potencia(self, n1, n2):
        return n1 ** n2
