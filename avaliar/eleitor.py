import socket
import threading
import json
import struct
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.votacao import Candidato, Voto, NotaInformativa

def escutar_multicast():
    group = '224.1.1.1'
    port = 5007
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    
    mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        try:
            dados, _ = sock.recvfrom(1024)
            nota_dict = json.loads(dados.decode('utf-8'))
            nota = NotaInformativa.from_dict(nota_dict)
            
            # Limpa um pouco a confusão visual
            print(f"\n\n [AVISO]: {nota.mensagem}")
            print(f"--- Envie seu voto agora")
            # Isso aqui é um "lembrete" visual que aparece logo abaixo da mensagem
            print("Sua opção (ID do prato): ", end="", flush=True) 
            
        except:
            break

def realizar_votacao():
    print("  --- SISTEMA DE VOTAÇÃO DELIVERY ---")
    
    # AJUSTE 1: Primeiro o login, sem interrupções
    login = input("Digite seu Login/Nome: ")
    
    # AJUSTE 2: Agora que já temos o nome, iniciamos a thread do Admin
    threading.Thread(target=escutar_multicast, daemon=True).start()

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('localhost', 12345))
        
        # 1. O servidor agora espera um JSON para diferenciar Admin de Eleitor
        pacote_login = json.dumps({"login": login})
        cliente.sendall(pacote_login.encode('utf-8'))
        
        # 2. Receber Lista de Candidatos
        tam_bytes = cliente.recv(4)
        tam = int.from_bytes(tam_bytes, 'big')
        lista_raw = cliente.recv(tam).decode('utf-8')
        candidatos = [Candidato.from_dict(c) for c in json.loads(lista_raw)]

        print("\n--- Cardápio para Votação ---")
        for c in candidatos:
            print(f"  [{c.id_candidato}] {c.nome} ({c.categoria})")

        # 3. Enviar Voto
        # Aqui, se o admin mandar mensagem, ela vai aparecer ANTES desse input
        escolha = int(input("\nSua opção (ID do prato): "))
        
        voto = Voto(login, escolha)
        cliente.sendall(json.dumps(voto.to_dict()).encode('utf-8'))

        # 4. Resposta do Servidor
        resposta = cliente.recv(1024).decode('utf-8')
        print(f"\n Servidor diz: {resposta}")

    except Exception as e:
        print(f"Erro na conexão: {e}")
    finally:
        print("\nSaindo do sistema...")
        cliente.close()

if __name__ == "__main__":
    realizar_votacao()