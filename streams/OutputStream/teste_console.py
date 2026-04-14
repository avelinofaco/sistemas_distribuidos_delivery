import sys
import os

# Ajuste de caminho para localizar models e streams
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.pedido import PedidoComida, PedidoBebida
from streams.OutputStream.Pedido_outputStream import PedidoJsonOutputStream

def rodar_teste_console():
    # Criando objetos para o teste
    pedidos = [
        PedidoComida(1, "Avelino", 45.0, "Pizza"),
        PedidoBebida(2, "Professor", 15.0, 300)
    ]

    # O destino é o sys.stdout.buffer (Saída Padrão Binária)
    escritor = PedidoJsonOutputStream(pedidos, len(pedidos), sys.stdout.buffer)
    
    # Ao rodar, você verá caracteres estranhos antes do JSON (são os 4 bytes do tamanho)
    escritor.write()

if __name__ == "__main__":
    rodar_teste_console()
