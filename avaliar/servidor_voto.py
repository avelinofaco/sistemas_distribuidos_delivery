import socket
import threading
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.votacao import Candidato, Voto, ComandoAdmin

# Configurações
LISTA_CANDIDATOS = [
    Candidato(1, "Pizza de Calabresa", "Comida"),
    Candidato(2, "Hambúrguer Gourmet", "Comida"),
    Candidato(3, "Suco de Laranja 500ml", "Bebida")
]

# VARIÁVEIS DE CONTROLE
TOTAL_VOTOS_ESPERADOS = 2
votos_atuais = 0
votos_lock = threading.Lock() # Garante que a contagem seja precisa entre as threads
votacao_aberta = True

def tratar_conexao(conn, addr):
    global LISTA_CANDIDATOS
    try:
        dados_brutos = conn.recv(1024).decode('utf-8')
        if not dados_brutos: return
        
        dados = json.loads(dados_brutos)

        # CENÁRIO ADMIN: ADD ou REMOVE
        if "acao" in dados:
            with votos_lock:
                if dados["acao"] == "ADD":
                    # Criamos o novo objeto e inserimos na lista
                    novo = Candidato(dados["id_candidato"], dados["nome"], dados["categoria"])
                    LISTA_CANDIDATOS.append(novo)
                
                elif dados["acao"] == "REMOVE":
                    # Filtramos para remover o item
                    LISTA_CANDIDATOS = [c for c in LISTA_CANDIDATOS if c.id_candidato != dados["id_candidato"]]

                # AGORA GERAMOS A RESPOSTA COM A LISTA JÁ ATUALIZADA
                lista_atualizada = [c.to_dict() for c in LISTA_CANDIDATOS]
                resposta_json = json.dumps(lista_atualizada)
                resposta_bytes = resposta_json.encode('utf-8')

                # Enviamos o tamanho (4 bytes) + o array JSON
                conn.sendall(len(resposta_bytes).to_bytes(4, 'big') + resposta_bytes)
            
            print(f"🛠️ Cardápio atualizado enviado para {addr}")
    
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()


def exibir_resultados():
    print("\n" + "="*40)
    print(" APURAÇÃO FINAL DOS VOTOS")
    print("="*40)
    
    total_votos = sum(c.votos for c in LISTA_CANDIDATOS)
    
    if total_votos == 0:
        print("Nenhum voto foi registrado no sistema.")
        return

    # 1. Encontrar o maior número de votos alcançado
    maior_voto = max(c.votos for c in LISTA_CANDIDATOS)
    
    # 2. Identificar todos os candidatos que possuem esse número (pode ser mais de um)
    vencedores = [c for c in LISTA_CANDIDATOS if c.votos == maior_voto]

    # 3. Exibir a listagem detalhada
    for c in LISTA_CANDIDATOS:
        perc = (c.votos / total_votos) * 100
        status = "⭐" if c in vencedores else "  "
        print(f"{status} {c.nome}: {c.votos} votos ({perc:.1f}%)")

    print("-" * 40)

    # 4. Tratar o Empate ou Vitória Única
    if len(vencedores) > 1:
        nomes_vencedores = " & ".join([v.nome for v in vencedores])
        print(f" EMPATE DETECTADO!")
        print(f"Os vencedores são: {nomes_vencedores}")
    else:
        print(f"🏆 VENCEDOR ÚNICO: {vencedores[0].nome.upper()}")
    

def tratar_eleitor(conn, addr):
    global votos_atuais, votacao_aberta
    try:
        # 1. Login
        login = conn.recv(1024).decode('utf-8')

        # 2. Enviar Lista
        lista_dto = [c.to_dict() for c in LISTA_CANDIDATOS]
        dados_lista = json.dumps(lista_dto).encode('utf-8')
        conn.sendall(len(dados_lista).to_bytes(4, 'big') + dados_lista)

        # 3. Receber Voto
        voto_bytes = conn.recv(1024)
        if voto_bytes and votacao_aberta:
            voto_data = json.loads(voto_bytes.decode('utf-8'))
            voto_obj = Voto.from_dict(voto_data)

            # Sincronização: apenas uma thread por vez mexe no contador
            with votos_lock:
                for c in LISTA_CANDIDATOS:
                    if c.id_candidato == voto_obj.id_candidato:
                        c.votos += 1
                        votos_atuais += 1
                        print(f" [{votos_atuais}/{TOTAL_VOTOS_ESPERADOS}] Voto de {voto_obj.eleitor} registrado.")
                
                # Se atingiu o limite, fecha a votação e mostra o resultado
                if votos_atuais >= TOTAL_VOTOS_ESPERADOS:
                    votacao_aberta = False
                    # Usamos um timer de 1s só para dar tempo do último cliente receber o OK
                    threading.Timer(1.0, exibir_resultados).start()

            conn.sendall(f"Obrigado {login}! Seu voto foi computado.".encode('utf-8'))
        else:
            conn.sendall("A votação já atingiu o limite de participantes.".encode('utf-8'))
            
    finally:
        conn.close()

def iniciar_servidor():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 12345))
    sock.listen(5)
    
    print(f" Servidor Multi-thread aguardando {TOTAL_VOTOS_ESPERADOS} votos...")

    while True:
        conn, addr = sock.accept()
        threading.Thread(target=tratar_eleitor, args=(conn, addr)).start()

if __name__ == "__main__":
    iniciar_servidor()