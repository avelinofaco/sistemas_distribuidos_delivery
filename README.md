#📡 Sistema Distribuído com Sockets, Streams e Votação de Delivery

Este projeto implementa um sistema distribuído completo, desenvolvido para a disciplina de Sistemas Distribuídos, abordando conceitos fundamentais como:

Comunicação via Sockets (TCP/UDP)
Streams personalizados (InputStream/OutputStream)
Serialização manual de dados
Representação externa (JSON)
Concorrência com multithreading
🎯## Objetivo

Desenvolver um sistema capaz de transmitir dados estruturados entre processos distribuídos, aplicando os conceitos teóricos em um cenário prático de votação e gerenciamento de pedidos.

🧩 Parte 1 — Sockets e Streams
✅### Questão 1 — Definição do Serviço Remoto

Foi desenvolvido um sistema de votação para cardápio de delivery, com interação entre eleitores e administradores.

📦 Classes POJO:
Candidato → itens disponíveis para votação
Voto → representa o voto do eleitor
ComandoAdmin → ações administrativas
Pedido → utilizado como base para manipulação de streams
⚙️ Classes de Serviço:
Gerenciamento de candidatos
Processamento de votos
Controle administrativo
✅### Questão 2 — OutputStream Personalizado

Foi implementada a classe:

PedidoOutputStream extends OutputStream
🔧 Responsabilidades:
Enviar um conjunto de objetos Pedido como fluxo de bytes
Realizar serialização manual
📥 Parâmetros do construtor:
Array de Pedido
Quantidade de objetos
Tamanho em bytes de pelo menos 3 atributos
Um OutputStream de destino
🧪 Testes realizados:
✔️ System.out
✔️ FileOutputStream
✔️ Socket TCP
✅### Questão 3 — InputStream Personalizado

🔧 Responsabilidades:
Ler fluxo de bytes
Reconstruir objetos Pedido (desserialização manual)
📥 Parâmetro do construtor:
Um InputStream de origem
🧪 Testes realizados:
✔️ System.in
✔️ FileInputStream
✔️ Socket TCP
🔄 Parte 2 — Serialização
✅### Questão 4 — Comunicação Cliente-Servidor com Pedido

Foi implementado um serviço remoto utilizando Sockets TCP, com troca de dados baseada na classe Pedido.

🔌 Comunicação:
Cliente ↔ Servidor via TCP
Troca de dados em formato de bytes
🔁 Fluxo de execução:

Cliente:

Serializa objeto Pedido
Empacota requisição
Envia ao servidor
Recebe resposta
Desserializa

Servidor:

Recebe requisição
Desserializa objeto Pedido
Processa lógica
Serializa resposta
Envia ao cliente
🛠️ Protocolo de Comunicação

Para garantir integridade dos dados:

Header (4 bytes): tamanho da mensagem
Payload: dados serializados
📦 Serialização
Implementação manual (byte a byte)
Controle total sobre envio e leitura dos dados
Baseada na classe Pedido
🌐## Parte 3 — Representação Externa de Dados
✅### Questão 5 — Sistema de Votação Distribuído

Foi desenvolvido um sistema completo de votação com comunicação híbrida.

🗳️## Funcionalidades

👤### Eleitor:
Login no sistema
Recebe lista de candidatos
Realiza votação

👨‍💼### Administrador:
Adiciona candidatos
Remove candidatos
Envia avisos informativos

⏱️### Controle de Votação
Tempo limite definido pelo servidor
Após o prazo:
Bloqueio de novos votos
Apuração automática
Definição do vencedor

📊 ### Processamento de Resultados
Total de votos por candidato
Percentual de votos
Identificação do vencedor

🏗️ ### Arquitetura de Comunicação
🔌 TCP (Unicast)
Login
Envio de votos
Lista de candidatos

📡 UDP (Multicast)
Envio de avisos administrativos
Grupo multicast: 224.1.1.1

🧵 Concorrência
Servidor multi-threaded
Uma thread por cliente
Suporte a múltiplas conexões simultâneas

🛠️ Representação de Dados
Utilização de JSON
(alternativa ao Protocol Buffers sugerido na atividade)

📢 ### Sistema de Notificações
Envio via multicast
Clientes recebem automaticamente
Comunicação eficiente e escalável

🧪 ###  Tecnologias Utilizadas
Java → Streams personalizados e serialização (Pedido)
Python → Sockets, Threads e JSON
TCP/UDP
Multithreading

📌 ### Resultados

✔️ Implementação completa das 5 questões
✔️ Uso correto de Pedido nas questões 2, 3 e 4
✔️ Comunicação cliente-servidor funcional
✔️ Streams personalizados operando corretamente
✔️ Sistema de votação distribuído robusto
✔️ Integração eficiente entre TCP e UDP

💡 ### Melhorias Futuras
Interface gráfica (Web/Desktop)
Persistência em banco de dados
Criptografia de dados
Implementação com Protocol Buffers
📚 ### Conclusão

O projeto demonstra, de forma prática, a aplicação de conceitos fundamentais de:

Sistemas distribuídos
Comunicação em rede
Serialização de dados
Concorrência
