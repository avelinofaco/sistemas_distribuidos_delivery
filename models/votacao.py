import json

class Candidato:
    """Representa um item do cardápio/candidato na votação."""
    def __init__(self, id_candidato: int, nome: str, categoria: str):
        self.id_candidato = id_candidato
        self.nome = nome
        self.categoria = categoria
        self.votos = 0 # Usado apenas no servidor para contagem

    def to_dict(self):
        return {
            "id_candidato": self.id_candidato,
            "nome": self.nome,
            "categoria": self.categoria
        }

    @staticmethod
    def from_dict(data: dict):
        return Candidato(
            data["id_candidato"],
            data["nome"],
            data["categoria"]
        )



class Voto:
    """Representa a intenção de voto de um eleitor/cliente."""
    def __init__(self, eleitor: str, id_candidato: int):
        self.eleitor = eleitor
        self.id_candidato = id_candidato

    def to_dict(self):
        return {
            "eleitor": self.eleitor,
            "id_candidato": self.id_candidato
        }

    @staticmethod
    def from_dict(data: dict):
        return Voto(data["eleitor"], data["id_candidato"])



class NotaInformativa:
    """Representa a mensagem multicast enviada pelo administrador."""
    def __init__(self, admin_nome: str, mensagem: str):
        self.admin_nome = admin_nome
        self.mensagem = mensagem

    def to_dict(self):
        return {
            "admin": self.admin_nome,
            "mensagem": self.mensagem,
            "tipo": "notificacao"
        }

    @staticmethod
    def from_dict(data: dict):
        return NotaInformativa(data["admin"], data["mensagem"])


class ComandoAdmin:
    """Representa uma ordem de alteração (Adicionar/Remover) vinda do Admin."""
    def __init__(self, acao: str, id_candidato: int = None, nome: str = None, categoria: str = None):
        self.acao = acao # "ADD" ou "REMOVE"
        self.id_candidato = id_candidato
        self.nome = nome
        self.categoria = categoria

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data: dict):
        return ComandoAdmin(**data) 
