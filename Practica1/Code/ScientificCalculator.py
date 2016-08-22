from Calculator import *

class ScientificCalculator(Calculator):
    
    def multiplica(self, n1, n2):
        return n1*n2

    def divide(self, n1,n2):
        if n2 == 0:
            return "error"
        else:
            return n1/n2

    def modulo(self,n1,n2):
        return n1%n2

    def cuadrado(self,n1,n2):
        if n2 == 0:
            return 1
        else:
            return n1 * (self.cuadrado(n1,n2-1))
