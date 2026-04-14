import socket
import json
import sys
import os

SERVER_HOST = "10.10.244.29"
SERVER_PORT = 12345
MULTICAST_GROUP = "224.1.1.1"
MULTICAST_PORT = 5007

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.votacao import NotaInformativa, ComandoAdmin

def gerenciar_candidatos():
    print("\n--- GERENCIAR CARDÁPIO ---")
    print("[1] Adicionar | [2] Remover | [0] Voltar")
    op = input("Escolha: ")
    if op not in ['1', '2']: return

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((MULTICAST_GROUP, SERVER_PORT))

        if op == '1':
            id_c = int(input("ID: "))
            nome = input("Nome: ")
            cat = input("Cat: ")
            cmd = {"acao": "ADD", "id_candidato": id_c, "nome": nome, "categoria": cat}
        else:
            id_c = int(input("ID p/ remover: "))
            cmd = {"acao": "REMOVE", "id_candidato": id_c}

        # 1. Enviar comando JSON
        cliente.sendall(json.dumps(cmd).encode('utf-8'))

        # 2. Receber resposta (Lendo os 4 bytes de tamanho primeiro)
        header = cliente.recv(4)
        if header:
            tamanho = int.from_bytes(header, 'big')
            # Lemos o corpo da mensagem com base no tamanho recebido
            corpo_bytes = cliente.recv(tamanho)
            lista_raw = corpo_bytes.decode('utf-8')

            # 3. EXIBIR NO CONSOLE (Exatamente como solicitado)
            print(f"🖥️ Servidor: {lista_raw}")
        else:
            print("❌ Servidor não retornou dados.")

    except Exception as e:
        print(f"❌ Erro no Admin: {e}")
    finally:
        cliente.close()
        
def enviar_multicast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    
    msg = input("Digite a nota para o grupo Multicast: ")
    nota = NotaInformativa("Gerente Avelino", msg)
    sock.sendto(json.dumps(nota.to_dict()).encode('utf-8'), (MULTICAST_GROUP, MULTICAST_PORT))
    print("📡 Aviso enviado!")

if __name__ == "__main__":
    while True:
        print("\n--- PAINEL ADMIN DELIVERY ---")
        print("1. Enviar Aviso (UDP Multicast)")
        print("2. Gerenciar Cardápio (TCP Unicast)")
        print("3. Sair")
        escolha = input("Opção: ")
        
        if escolha == '1': enviar_multicast()
        elif escolha == '2': gerenciar_candidatos()
        elif escolha == '3': break