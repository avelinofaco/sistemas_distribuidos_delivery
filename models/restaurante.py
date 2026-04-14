from typing import List
from pedido import Pedido
    
# Agregação: Restaurante
class Restaurante:
    def __init__(self, nome: str):
        self.nome = nome
        self.pedidos: List[Pedido] = []

    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)