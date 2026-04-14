import sys
import os

# Ajuste de caminho para a raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.pedido import PedidoComida, PedidoBebida
from streams.OutputStream.Pedido_outputStream import PedidoJsonOutputStream

def gerar_arquivo():
    caminho = "../../pedidos.json"
    
    # Criando os dados
    pedidos = [
        PedidoComida(10, "Avelino", 85.0, "Combo Japonês"),
        PedidoBebida(11, "Maria", 10.0, 350),
        PedidoComida(12, "Jose", 30.0, "X-Burger")
    ]

    print(f"--- Gerando Arquivo: {caminho} ---")
    
    # IMPORTANTE: "wb" para escrita binária
    with open(caminho, "wb") as f:
        escritor = PedidoJsonOutputStream(pedidos, len(pedidos), f)
        escritor.write()
        
    print(f" Sucesso! Arquivo gerado com {os.path.getsize(caminho)} bytes.")

if __name__ == "__main__":
    gerar_arquivo()