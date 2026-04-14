from abc import ABC, abstractmethod

# Interface: Avaliável
class Avaliavel(ABC):
    @abstractmethod
    def avaliar(self, nota: int, comentario: str):
        pass

# Superclasse: Pedido
class Pedido(Avaliavel):
    def __init__(self, id_pedido: int, cliente: str, valor: float):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.valor = valor
        self.nota = 0
        self.comentario = ""

    def avaliar(self, nota: int, comentario: str):
        self.nota = nota
        self.comentario = comentario

    #  SERIALIZAÇÃO
    def to_dict(self):
        return {
            "id_pedido": self.id_pedido,
            "cliente": self.cliente,
            "valor": self.valor,
            "nota": self.nota,
            "comentario": self.comentario
        }

    #  DESSERIALIZAÇÃO (FACTORY)
    @staticmethod
    def from_dict(data: dict):
        tipo = data.get("tipo")

        if tipo == "comida":
            obj = PedidoComida(
                data["id_pedido"],
                data["cliente"],
                data["valor"],
                data["prato"]
            )

        elif tipo == "bebida":
            obj = PedidoBebida(
                data["id_pedido"],
                data["cliente"],
                data["valor"],
                data["volume_ml"]
            )

        elif tipo == "sobremesa":
            obj = PedidoSobremesa(
                data["id_pedido"],
                data["cliente"],
                data["valor"],
                data["doce"]
            )
        else:
            raise ValueError("Tipo inválido")

        obj.nota = data.get("nota", 0)
        obj.comentario = data.get("comentario", "")

        return obj

# Subclasse: PedidoComida
class PedidoComida(Pedido):
    def __init__(self, id_pedido, cliente, valor, prato: str):
        super().__init__(id_pedido, cliente, valor)
        self.prato = prato

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "tipo": "comida",
            "prato": self.prato
        })
        return data

# Subclasse: PedidoBebida
class PedidoBebida(Pedido):
    def __init__(self, id_pedido, cliente, valor, volume_ml: int):
        super().__init__(id_pedido, cliente, valor)
        self.volume_ml = volume_ml

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "tipo": "bebida",
            "volume_ml": self.volume_ml
        })
        return data
    
# Subclasse: PedidoSobremesa
class PedidoSobremesa(Pedido):
    def __init__(self, id_pedido, cliente, valor, doce: str):
        super().__init__(id_pedido, cliente, valor)
        self.doce = doce

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "tipo": "sobremesa",
            "doce": self.doce
        })
        return data
    