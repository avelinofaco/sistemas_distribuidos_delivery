import json
from models.pedido import Pedido

class PedidoJsonInputStream:
    def __init__(self, origem):
        self.origem = origem

    def ler_pedido(self):
        # Lê os 4 bytes do prefixo de tamanho
        tamanho_bytes = self.origem.read(4)
        if not tamanho_bytes or len(tamanho_bytes) < 4:
            return None
            
        tamanho = int.from_bytes(tamanho_bytes, 'big')
        
        # Lê exatamente a quantidade de bytes do JSON
        corpo_json = self.origem.read(tamanho)
        if not corpo_json:
            return None
            
        try:
        # Tenta decodificar
            corpo_json_str = corpo_json.decode('utf-8')
            return Pedido.from_dict(json.loads(corpo_json_str))
        except (json.JSONDecodeError, UnicodeDecodeError):
        # Se os dados forem lixo (como digitar no teclado), ele apenas ignora
            return None