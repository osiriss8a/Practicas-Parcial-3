
class Validar():
     def __init__(self):
        self.index = 0

     def ValidarLetra(self, valor):
        # Retorna True si todas las letras son minúsculas (ASCII 97-122)
        for i in valor:
            if not ((65 <= ord(i) <= 90) or (97 <= ord(i) <= 122)):
                return False
        return True

     def ValidarNumeros(self, valor):
        # Retorna True si todos los caracteres son números (ASCII 48-57)
        for i in valor:
            if not (48 <= ord(i) <= 57):
                return False
        return True