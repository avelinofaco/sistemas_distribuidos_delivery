import json

class PedidoJsonOutputStream:
    def __init__(self, pedidos: list, num_objetos: int, destino):
        self.pedidos = pedidos[:num_objetos]
        self.destino = destino

    def write(self):
        for pedido in self.pedidos:
            dados_dict = pedido.to_dict()
            json_bytes = json.dumps(dados_dict).encode('utf-8')
            
            # ITEM 2.iii: Enviando o número de bytes antes do conteúdo
            # Usamos 4 bytes em formato 'big-endian' para o tamanho
            tamanho = len(json_bytes)
            self.destino.write(tamanho.to_bytes(4, 'big'))
            
            # Enviamos o JSON propriamente dito
            self.destino.write(json_bytes)
            
        if hasattr(self.destino, 'flush'):
            self.destino.flush()