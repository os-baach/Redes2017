import Calculator

class Parser:

    def __init__(self, entrada):
        self.entrada = entrada.replace(" ","")
        i = 1
        while(self.__esnumero(self.entrada[0:i])):
            i += 1
        self.numero1 = int(self.entrada[0:i-1])
        self.operador = self.entrada[i]
        self.numero2 = int(self.entrada[i+1:])



    def __esnumero(self,cadena):
        try:
            val = int(cadena)
            return True
        except ValueError:
            return False


  
