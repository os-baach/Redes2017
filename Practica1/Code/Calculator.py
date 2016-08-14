# Clase que representa a una calculadora que suma y resta
class Calculator:
    
    # Suma
    def suma(self, n1, n2):
        return n1+n2
        
    # Resta
    def resta(self, n1, n2):
        return n1-n2
        
    # Encripta una contraseña
    def encripta_contrasena(self, contrasena):
        nueva_contrasena = ''
        for caracter in contrasena:
            nueva_contrasena += chr((ord(caracter) + 5))
        return nueva_contrasena

        
