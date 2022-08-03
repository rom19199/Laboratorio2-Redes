import socket
import pickle
from Emisor import Aplicacion
from Checksum import checkReceiverChecksum, printingResults

HOST = "127.0.0.1"  #Direccion loopback
PORT = 65123        # > 1023 (Puerto escucha)
HEADER = 10 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    try:
        with conn:
            print(f"Conectado a {addr[0]}:{addr[1]} ")
            while True:
                data_len = conn.recv(HEADER)

                if not data_len:
                    break
                else:
                    data = b''
                    data += conn.recv(int(data_len))
                    data_deserial = pickle.loads(data)
                    print(data_deserial.mensaje())
                    print(data_deserial.mensajeR())
                    data_deserial.setCheckReciever(checkReceiverChecksum(data_deserial.mensajeR().to01(), 8, data_deserial.getCheckSum()))
                    printingResults(data_deserial.getCheckSum(), data_deserial.getCheckReciever())
                
    except KeyboardInterrupt:       #Ctrl + C
        pass

print("Cerrando conexion")