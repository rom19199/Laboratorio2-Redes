# import zlib and crc32
from http import server
import zlib
from bitarray import bitarray
from socket import *
from server import HOST, PORT
import binascii
import time

class Verify():
    def __init__(self, algoritmo):
        self.m_bit = ""
        self.m_original = ""
        self.algoritmo = algoritmo #CRC32
        self.m_rec = ""
        

    def recibir_cadena_segura(self, m_bit, m_original):
     start = time.time()

     self.m_original = m_original

     if self.algoritmo == "CRC32":
       j = self.check_CRC32(m_bit)
       print(j)
       if j == '000':
         print('verificacion')
       else:
         print('Error, ruido')

       self.m_bit = m_bit[:-3]
     else: 
       self.m_bit = m_bit
        
       correction = server.detectError(m_bit, int(m_original))
       if correction > 0:
         print("El error se encuentra en:" + str(correction))
       else: 
         print("Felicidades")

     end = time.time()

#https://python.hotexamples.com/es/examples/kafka.util/-/crc32/python-crc32-function-examples.html
    def checkCRC32(self, b):
      a = b
      d = '1001'
      c = a[:4]
    
      j = self.operar_xor(c,d)    

      for x in range(4,len(a)):
          c = j + a[x]
          if c[0] == '1':
             j = self.operar_xor(c,d)
          else:
             temp = c[1:]
             j = temp
      return j
