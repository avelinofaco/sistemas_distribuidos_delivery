📡 Sistema Distribuído com Sockets, Streams e Votação de Delivery
📖 Descrição

Este projeto implementa um sistema distribuído que integra conceitos fundamentais de:

Comunicação via Sockets (TCP/UDP)
Streams personalizados (InputStream/OutputStream)
Serialização manual de dados
Representação externa (JSON)
Concorrência (multithreading)

A aplicação principal consiste em um sistema de votação para cardápio de delivery, onde usuários votam em itens e administradores gerenciam o sistema.

🎯 Objetivo

Aplicar na prática os conceitos de sistemas distribuídos, implementando:

Transmissão de dados via streams
Comunicação cliente-servidor
Serialização e desserialização manual
Sistema real de votação com múltiplos clientes
🧩 Estrutura das Questões
✅ Questão 1 — Serviço Remoto

Foi definido um sistema de votação com as seguintes classes POJO:

Candidato
Voto
ComandoAdmin
Pedido (utilizada nas questões seguintes)

Também foram implementadas classes de serviço para:

Processamento de votos
Gerenciamento de candidatos
Controle administrativo
✅ Questão 2 — OutputStream personalizado

Implementação da classe:

PedidoOutputStream

Responsável por enviar um conjunto de objetos Pedido.

Características:

Recebe:
Array de Pedido
Quantidade de objetos
Tamanho em bytes de pelo menos 3 atributos
Um OutputStream de destino
Realiza serialização manual dos dados

Testes realizados:

System.out
FileOutputStream
Socket TCP
✅ Questão 3 — InputStream personalizado

Implementação da classe:

PedidoInputStream

Responsável por ler e reconstruir objetos Pedido.

Características:

Recebe um InputStream
Realiza leitura e desserialização manual

Testes realizados:

System.in
FileInputStream
Socket TCP
✅ Questão 4 — Serialização com Cliente-Servidor

Foi implementado um serviço remoto utilizando Sockets TCP, baseado na classe Pedido.

Funcionamento:

Cliente:
Serializa objetos Pedido
Envia requisição
Recebe resposta
Desserializa os dados
Servidor:
Recebe dados
Desserializa Pedido
Processa requisição
Serializa resposta
Envia ao cliente

Protocolo utilizado:

Header de 4 bytes → tamanho da mensagem
Payload → dados serializados
✅ Questão 5 — Sistema de Votação Distribuído

Sistema completo com comunicação híbrida:

Funcionalidades

Eleitor:

Login
Recebe lista de candidatos
Realiza voto

Administrador:

Adiciona/remove candidatos
Envia avisos informativos
Arquitetura
TCP (Unicast):
Login
Votação
Lista de candidatos
UDP (Multicast):
Envio de avisos
Grupo: 224.1.1.1
Concorrência
Servidor multi-threaded
Uma thread por cliente
Suporte a múltiplas conexões simultâneas
Controle de Votação
Tempo limite definido pelo servidor
Após o prazo:
Bloqueio de votos
Apuração automática
Cálculo de percentuais
Definição do vencedor
Representação de Dados
Utilização de JSON para troca de mensagens
(alternativa ao Protocol Buffers sugerido)
🛠️ Tecnologias Utilizadas
Java (Streams personalizados e serialização com Pedido)
Python (Sockets, Threads, JSON)
TCP/UDP
Multithreading
