📡 Sistema Distribuído com Sockets, Streams e Votação de Delivery

Este projeto implementa um sistema distribuído completo abordando:

Sockets (TCP/UDP)
Streams personalizados
Serialização manual
Representação externa de dados (JSON)
Concorrência (multithreading)
🧩 Sockets e Streams
✅ 1. Definição do Serviço Remoto

Foi desenvolvido um sistema de votação para cardápio de delivery, permitindo interação entre eleitores e administradores.

📦 Classes POJO criadas:
Candidato → representa itens do cardápio
Voto → representa votos realizados
ComandoAdmin → ações administrativas
Pedido → representa pedidos (base das questões 2, 3 e 4)
⚙️ Classes de Serviço:
Gerenciamento de candidatos
Processamento de votos
Controle administrativo
✅ 2. Implementação do OutputStream (Baseado em Pedido)

Foi criada a subclasse:

📤 PedidoOutputStream

Extende OutputStream e é responsável por enviar um conjunto de objetos Pedido.

✔️ Construtor recebe:
Array de objetos Pedido
Quantidade de objetos a serem enviados
Tamanho em bytes de pelo menos 3 atributos (ex: id, descrição, valor)
Um OutputStream de destino
⚙️ Funcionamento:
Serializa manualmente os objetos Pedido em bytes
Garante envio estruturado dos dados
🧪 Testes realizados:
✔️ System.out
✔️ FileOutputStream
✔️ Socket TCP
✅ 3. Implementação do InputStream (Baseado em Pedido)

Foi criada a subclasse:

📥 PedidoInputStream

Responsável por ler e reconstruir objetos Pedido.

✔️ Construtor:
Recebe um InputStream de origem
⚙️ Funcionamento:
Lê os bytes do stream
Desserializa manualmente
Reconstrói os objetos Pedido
🧪 Testes realizados:
✔️ System.in
✔️ FileInputStream
✔️ Socket TCP
🔄 Serialização
✅ 4. Serviço Cliente-Servidor (Baseado em Pedido)

Também foi implementado um serviço remoto utilizando a classe Pedido como base para troca de dados.

🔌 Comunicação:
Utilização de Sockets TCP
Troca de dados via fluxo de bytes
🔁 Fluxo de Comunicação:
💻 Cliente:
Serializa objetos Pedido
Empacota a requisição
Envia ao servidor
Recebe resposta
Desserializa os dados
🖥️ Servidor:
Recebe requisição
Desserializa Pedido
Processa a lógica (ex: registrar pedido)
Serializa resposta
Envia ao cliente
🛠️ Protocolo de Comunicação
Header (4 bytes): tamanho da mensagem
Payload: dados serializados
📦 Serialização utilizada:
Serialização manual dos objetos Pedido
Controle explícito dos bytes enviados
Reconstrução no lado servidor/cliente
🌐 Representação Externa de Dados
✅ 5. Sistema de Votação Distribuído

Sistema completo de votação com comunicação híbrida.

🗳️ Funcionalidades
👤 Eleitor:
Login
Recebe lista de candidatos
Vota
👨‍💼 Administrador:
Adiciona/remove candidatos
Envia avisos
⏱️ Controle de Tempo
Tempo limite para votação
Após o prazo:
Bloqueio de votos
Apuração automática
Definição do vencedor
📊 Processamento
Total de votos
Percentuais
Candidato vencedor
🏗️ Arquitetura
🔌 TCP (Unicast)
Login
Votação
Lista de candidatos
📡 UDP (Multicast)
Avisos administrativos
Grupo: 224.1.1.1
🧵 Concorrência
Servidor multi-threaded
Uma thread por cliente
Execução simultânea de votos
🛠️ Representação de Dados
Utilização de JSON
(alternativa ao Protocol Buffers)
📢 Notificações
Envio via multicast
Clientes recebem automaticamente
🧪 Tecnologias Utilizadas
Java (Streams e serialização com Pedido)
Python (Sockets, Threads, JSON)
TCP/UDP
Multithreading
