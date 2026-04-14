import socket
import threading
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.votacao import Candidato, Voto

HOST = '0.0.0.0'   # aceita conexão de outras máquinas
PORT = 12345

LISTA_CANDIDATOS = [
    Candidato(1, "Pizza de Calabresa", "Comida"),
    Candidato(2, "Hambúrguer Gourmet", "Comida"),
    Candidato(3, "Suco de Laranja 500ml", "Bebida")
]

TOTAL_VOTOS_ESPERADOS = 2
votos_atuais = 0
votos_lock = threading.Lock()
votacao_aberta = True


def enviar_json_com_tamanho(conn, obj):
    payload = json.dumps(obj).encode('utf-8')
    conn.sendall(len(payload).to_bytes(4, 'big') + payload)


def exibir_resultados():
    print("\n" + "=" * 40)
    print("APURAÇÃO FINAL DOS VOTOS")
    print("=" * 40)

    total_votos = sum(c.votos for c in LISTA_CANDIDATOS)

    if total_votos == 0:
        print("Nenhum voto foi registrado.")
        return

    maior_voto = max(c.votos for c in LISTA_CANDIDATOS)
    vencedores = [c for c in LISTA_CANDIDATOS if c.votos == maior_voto]

    for c in LISTA_CANDIDATOS:
        perc = (c.votos / total_votos) * 100
        status = "⭐" if c in vencedores else " "
        print(f"{status} {c.nome}: {c.votos} votos ({perc:.1f}%)")

    print("-" * 40)

    if len(vencedores) > 1:
        nomes = " & ".join(v.nome for v in vencedores)
        print(f"EMPATE: {nomes}")
    else:
        print(f"VENCEDOR: {vencedores[0].nome}")


def tratar_conexao(conn, addr):
    global LISTA_CANDIDATOS, votos_atuais, votacao_aberta

    try:
        dados_brutos = conn.recv(4096).decode('utf-8')
        if not dados_brutos:
            return

        dados = json.loads(dados_brutos)

        # ADMIN
        if "acao" in dados:
            with votos_lock:
                if dados["acao"] == "ADD":
                    novo = Candidato(
                        dados["id_candidato"],
                        dados["nome"],
                        dados["categoria"]
                    )
                    LISTA_CANDIDATOS.append(novo)

                elif dados["acao"] == "REMOVE":
                    LISTA_CANDIDATOS = [
                        c for c in LISTA_CANDIDATOS
                        if c.id_candidato != dados["id_candidato"]
                    ]

                lista_atualizada = [c.to_dict() for c in LISTA_CANDIDATOS]

            enviar_json_com_tamanho(conn, lista_atualizada)
            print(f"[ADMIN] Cardápio atualizado para {addr}")
            return

        # ELEITOR
        login = dados.get("login", "Anônimo")

        lista_dto = [c.to_dict() for c in LISTA_CANDIDATOS]
        enviar_json_com_tamanho(conn, lista_dto)

        voto_bytes = conn.recv(4096)
        if voto_bytes and votacao_aberta:
            voto_data = json.loads(voto_bytes.decode('utf-8'))
            voto_obj = Voto.from_dict(voto_data)

            with votos_lock:
                for c in LISTA_CANDIDATOS:
                    if c.id_candidato == voto_obj.id_candidato:
                        c.votos += 1
                        votos_atuais += 1
                        print(f"[{votos_atuais}/{TOTAL_VOTOS_ESPERADOS}] Voto de {voto_obj.eleitor} registrado.")
                        break

                if votos_atuais >= TOTAL_VOTOS_ESPERADOS:
                    votacao_aberta = False
                    threading.Timer(1.0, exibir_resultados).start()

            conn.sendall(f"Obrigado {login}! Seu voto foi computado.".encode('utf-8'))
        else:
            conn.sendall("A votação já foi encerrada.".encode('utf-8'))

    except Exception as e:
        print(f"Erro com {addr}: {e}")

    finally:
        conn.close()


def iniciar_servidor():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"Servidor ouvindo em {HOST}:{PORT} e aguardando {TOTAL_VOTOS_ESPERADOS} votos...")

    while True:
        conn, addr = sock.accept()
        threading.Thread(target=tratar_conexao, args=(conn, addr), daemon=True).start()


if __name__ == "__main__":
    iniciar_servidor()