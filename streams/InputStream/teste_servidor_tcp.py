import socket
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from streams.InputStream.Pedido_InputStream import PedidoJsonInputStream

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(('localhost', 12345))
    servidor.listen(1)
    print(" Servidor aguardando Requests...\n")

    while True:
        conn, addr = servidor.accept()
        print(f" Conectado a {addr}")
        
        try:
            # 1. Recebe e Desempacota (Request)
            stream_in = conn.makefile('rb')
            leitor = PedidoJsonInputStream(stream_in)
            pedidos_recebidos = []
            
            while True:
                obj = leitor.ler_pedido()
                if not obj: break
                pedidos_recebidos.append(obj)
                print(f" Processando: {type(obj).__name__} de {obj.cliente}")

            # 2. Prepara e Empacota a Resposta (Reply) - REQUISITO 4
            reply = {
                "status": "sucesso",
                "total_processado": len(pedidos_recebidos),
                "mensagem": "Cozinha avisada!"
            }
            reply_bytes = json.dumps(reply).encode('utf-8')
            
            # Enviamos o tamanho (4 bytes) + o corpo do reply
            conn.sendall(len(reply_bytes).to_bytes(4, 'big') + reply_bytes)
            print(" Reply enviado ao cliente.")

        finally:
            conn.close()

if __name__ == "__main__":
    iniciar_servidor()