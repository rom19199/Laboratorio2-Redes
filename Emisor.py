
#Clase donde se recibe la cadena de texto de entrada
class Aplicacion:

    def __init__(self, texto):
        #print("Escriba la cadena de texto")
        #self.cadena = input("Escriba la cadena de texto: ")
        self.texto = texto
        
        
        
    def mensaje(self):
        print(f"El mensaje es, {self.texto}")
        

cadena = input("Ingrese la cadena: ")
text = Aplicacion(cadena)
text.mensaje()

