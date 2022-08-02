from bitarray import bitarray
from random import random

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
        arr = bitarray(res)      
        self.texto = arr
        print(self.texto)
        return self.texto
    
    #  def bitarray(self):
    #      #str2ba = ba.frombytes(f"{self.texto}".encode('utf-8'))
    #      str2ba = arr.frombytes({self.texto}.encode('utf-8'))
    #      return str2ba
        
class Ruido(Aplicacion):
    def agregarRuido(self):
        j = 0
        for i in self.texto:
            a = self.texto[j]
            a = self.modificacion(a)
            self.texto[j] = a
            j+= 1
        print(self.texto)

    def prob(self):
        rand = random()
        return (rand > 0.5)

    def modificacion(self, valor):
        if self.prob():
            if valor == 0: 
                return 1
            else:
                return 0
        else:
            return valor             

#input del str
cadena = input("Ingrese la cadena: ")
text = Aplicacion(cadena)
texto = text.mensaje()
print("la cadena es: ", texto)

verificacion = Verificacion(texto)
texto = verificacion.str2binary() 

ruido = Ruido(texto)
ruido.agregarRuido()

