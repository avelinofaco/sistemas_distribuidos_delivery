import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from streams.InputStream.Pedido_InputStream import PedidoJsonInputStream

def ler_do_arquivo():
    caminho = "../../pedidos.json"
    
    print(f"--- Lendo do Arquivo: {caminho} ---\n")
    
    if not os.path.exists(caminho):
        print(" Erro: Arquivo não encontrado! Rode o script de saída primeiro.")
        return

    # IMPORTANTE: "rb" para leitura binária
    with open(caminho, "rb") as f:
        leitor = PedidoJsonInputStream(f)
        
        while True:
            obj = leitor.ler_pedido()
            if not obj:
                break
            
            # Aqui provamos que o objeto voltou a ser o que era
            tipo = type(obj).__name__
            print(f" Objeto Recuperado: {tipo} | Cliente: {obj.cliente} | Valor: R$ {obj.valor}")

    print("\n--- Fim da Leitura ---")

if __name__ == "__main__":
    ler_do_arquivo()