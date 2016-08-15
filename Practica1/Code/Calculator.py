import os
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

    # Verifica que el usuario esté registrado
    # Formato del archivo: usuario contraseña\n
    def busca_usuario(self, usuario, contrasena):
        crip = self.encripta_contrasena(contrasena)
        archivo = open(os.path.dirname(os.path.realpath(__file__)) + '/Input.txt', 'r')
        linea = archivo.readline()
        while linea: # Mientras no hayamos llegado al final del archivo
            lista = linea.split(' ')
            if lista[0] == usuario and lista[1] == crip:
                archivo.close()
                return True
            elif lista[0] == usuario:
                archivo.close()
                raise ValueError('Contraseña incorrecta')
            linea = archivo.readline()
        archivo.close()
        return False

    # Registra a un usuario para usar la calculadora
    def registra(self, usuario, contrasena):
        # Primero vemos que el usuario no esté registrado
        archivo = open(os.path.dirname(os.path.realpath(__file__)) + '/Input.txt',  'r+')
        linea = archivo.readline()
        while linea: # Mientras no hayamos llegado al final del archivo
            lista = linea.split(' ')
            if lista[0] == usuario:
                archivo.close()
                raise ValueError('El usuario ya está registrado')
            linea = archivo.readline()
        archivo.write(usuario + ' ' + self.encripta_contrasena(contrasena) + ' ' + '\n')
        archivo.close()
        
        
