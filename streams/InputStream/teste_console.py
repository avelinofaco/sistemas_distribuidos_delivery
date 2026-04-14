import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from streams.InputStream.Pedido_InputStream import PedidoJsonInputStream

def rodar_teste_entrada():
    # O InputStream de origem é o sys.stdin.buffer
    # Requisito 3.b
    leitor = PedidoJsonInputStream(sys.stdin.buffer)

    print("--- Aguardando dados via STDIN (Use piping para testar) ---", file=sys.stderr)

    while True:
        pedido = leitor.ler_pedido()
        if not pedido:
            break
        
        # Exibindo o que foi recuperado
        print(f" Recebido via Console: {pedido.cliente} comprou {type(pedido).__name__}", file=sys.stderr)

if __name__ == "__main__":
    rodar_teste_entrada()