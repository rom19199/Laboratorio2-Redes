from bitarray import bitarray

#Clase donde se recibe la cadena de texto de entrada
class Aplicacion:

    def __init__(self, texto):
        #print("Escriba la cadena de texto")
        #self.cadena = input("Escriba la cadena de texto: ")
        self.texto = texto
        
    def mensaje(self):
        #print(f"El mensaje es, {self.texto}")
        return self.texto
        
        

class Verificacion(Aplicacion):
     #Covertir str to binary ascii
     def str2binary(self):
        res = ''.join(format(ord(i), '08b') for i in self.texto)
        return str(res)
    
    #  def bitarray(self):
    #      arr = bitarray()      
    #      #str2ba = ba.frombytes(f"{self.texto}".encode('utf-8'))
    #      str2ba = arr.frombytes({self.texto}.encode('utf-8'))
    #      return str2ba
        


#input del str
cadena = input("Ingrese la cadena: ")
text = Aplicacion(cadena)
texto = text.mensaje()
print("la cadena es: ", texto)

verificacion = Verificacion(texto)
print("bin", verificacion.str2binary())   

