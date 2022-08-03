from bitarray import bitarray
from random import random

#Clase donde se recibe la cadena de texto de entrada
class Aplicacion:

    def __init__(self, texto):
        #print("Escriba la cadena de texto")
        #self.cadena = input("Escriba la cadena de texto: ")
        self.texto = texto
        self.textoR = None
        self.lenArr = None
        
    def mensaje(self):
        #print(f"El mensaje es, {self.texto}")
        return self.texto

    def mensajeR(self):
        return self.textoR

    def getlen(self):
        return self.lenArr

    def setTexto(self, texto):
        self.texto = texto

    def setTextoR(self, textoR):
        self.textoR = textoR

    def setlen(self, texto):
        self.lenArr = texto
        
        

class Verificacion(Aplicacion):
     #Covertir str to binary ascii
     def str2binary(self):
        res = ''.join(format(ord(i), '08b') for i in self.texto)
        arr = bitarray(res)
        arr1 = bitarray(res)
        lenArr = len(arr)   
        return arr, arr1, lenArr
    
        
class Ruido:
    def agregarRuido(self, texto):
        j = 0
        for i in texto:
            a = texto[j]
            a = self.modificacion(a)
            texto[j] = a
            j+= 1
        # print (texto)
        return texto

    def prob(self):
        rand = random()
        return (rand <= 0.01)


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
texto, textoR, lenArr = verificacion.str2binary() 
text.setTexto(texto)
text.setTextoR(textoR)
text.setlen(lenArr)

ruido = Ruido()
textoR = ruido.agregarRuido(text.mensajeR())
text.setTextoR(textoR)
print(text.mensaje())
print(text.getlen())
