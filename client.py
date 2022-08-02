import socket
import time
import pickle
from Emisor import Aplicacion, Verificacion, Ruido

HOST = "127.0.0.1"          #IP del servidor
PORT = 65123                #Puerto de envio
HEADER = 10


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    #input del str
    cadena = input("Ingrese la cadena: ")
    text = Aplicacion(cadena)
    texto = text.mensaje()
    print("la cadena es: ", texto)

    verificacion = Verificacion(texto)
    texto = verificacion.str2binary() 

    ruido = Ruido(texto)
    ruido.agregarRuido()

    names = [100, 
             'Maria', 
             'Rodrigo',  
             3.1416, 
             'Juan', 
             'Nabucodonosor', 
             'Sandro',
             (1+3j)]

    data_serial = pickle.dumps(text)

    #<HEADER><PAYLOAD>
    data_len = str(len(data_serial))

    data = bytes(f"{data_len:<{HEADER}}",'utf-8') + data_serial
    print(data)
    s.send(data)