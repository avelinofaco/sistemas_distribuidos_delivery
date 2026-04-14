import socket
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.pedido import PedidoComida, PedidoBebida
from streams.OutputStream.Pedido_outputStream import PedidoJsonOutputStream

def rodar_cliente():
    pedidos = [
        PedidoComida(50, "Avelino", 60.0, "Sushi"),
        PedidoBebida(51, "Avelino", 12.0, 1000)
    ]

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect(('localhost', 12345))
        
        # 1. Empacota e Envia (Request)
        stream_saida = cliente.makefile('wb')
        sender = PedidoJsonOutputStream(pedidos, len(pedidos), stream_saida)
        sender.write()
        stream_saida.flush()
        
        # Avisa ao servidor que terminamos de enviar o Request
        cliente.shutdown(socket.SHUT_WR)

        # 2. Recebe e Desempacota a Resposta (Reply) - REQUISITO 4
        # Lendo o prefixo de 4 bytes do tamanho do reply
        tam_reply_bytes = cliente.recv(4)
        if tam_reply_bytes:
            tam_reply = int.from_bytes(tam_reply_bytes, 'big')
            corpo_reply = cliente.recv(tam_reply)
            
            # Desempacotando a mensagem de reply
            reply_dict = json.loads(corpo_reply.decode('utf-8'))
            print(f"\n RESPOSTA DO SERVIDOR: {reply_dict['mensagem']}")
            print(f" Status: {reply_dict['status']} | Total: {reply_dict['total_processado']}")

    finally:
        cliente.close()

if __name__ == "__main__":
    rodar_cliente()