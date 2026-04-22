# 📡 Sistema Distribuído com Sockets, Streams e Votação de Delivery

![Python](https://img.shields.io/badge/Python-Sockets-blue)
![Protocol](https://img.shields.io/badge/Protocol-TCP%2FUDP-green)
![Architecture](https://img.shields.io/badge/Architecture-Distributed-black)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🚀 Visão Geral

Este projeto apresenta a implementação de um **sistema distribuído completo em Python**, desenvolvido para demonstrar na prática conceitos fundamentais de comunicação em rede, serialização de dados e concorrência.

A solução simula um ambiente real de **votação de cardápio de delivery**, permitindo interação simultânea entre clientes e administradores.

---

## 🎯 Objetivos

- Implementar comunicação cliente-servidor via **Sockets (TCP/UDP)**
- Criar mecanismos de envio e leitura de dados (streams)
- Aplicar **serialização manual de objetos**
- Construir um sistema distribuído com **concorrência**
- Simular um cenário real de aplicação (votação + pedidos)

---

## 🧩 Arquitetura do Sistema

O sistema foi dividido em três módulos principais:

### 🔹 1. Sockets e Streams
Manipulação de dados em baixo nível utilizando envio e leitura de bytes.

### 🔹 2. Serialização
Empacotamento e transmissão de objetos (`Pedido`) via rede.

### 🔹 3. Sistema Distribuído de Votação
Aplicação prática utilizando TCP + UDP + Multithreading.

---

## 🧱 Modelagem de Dados

As seguintes classes foram utilizadas:

- `Pedido` → base para serialização e comunicação  
- `Candidato` → itens disponíveis para votação  
- `Voto` → representa o voto do usuário  
- `ComandoAdmin` → ações administrativas  

---

## 🔄 Manipulação de Streams (Python)

Embora Python não utilize diretamente `InputStream/OutputStream` como Java, o projeto implementa o mesmo conceito através de:

### 📤 Envio de Dados (`PedidoOutputStream`)

Responsável por:

- Serializar objetos `Pedido` manualmente
- Converter dados para bytes
- Enviar via diferentes destinos

**Testes realizados:**
- Saída padrão (`print`)
- Arquivo (`open(..., 'wb')`)
- Socket TCP

---

### 📥 Leitura de Dados (`PedidoInputStream`)

Responsável por:

- Ler bytes de diferentes fontes
- Desserializar dados
- Reconstruir objetos `Pedido`

**Testes realizados:**
- Entrada padrão
- Arquivo (`open(..., 'rb')`)
- Socket TCP

---

## 🔌 Comunicação Cliente-Servidor

### 🧠 Baseada na classe `Pedido`

A comunicação foi implementada utilizando **Sockets TCP**, com troca de dados em formato binário.

### 🔁 Fluxo

**Cliente:**
- Serializa `Pedido`
- Envia requisição
- Recebe resposta
- Desserializa dados

**Servidor:**
- Recebe requisição
- Desserializa
- Processa
- Serializa resposta
- Envia ao cliente

---

## 🛠️ Protocolo de Comunicação

Para garantir robustez e evitar erros de transmissão:

- **Header (4 bytes)** → tamanho da mensagem  
- **Payload** → dados serializados (JSON/binário)  

---

## 🌐 Sistema de Votação Distribuído

### 🗳️ Funcionalidades

#### 👤 Eleitor
- Login no sistema  
- Visualização de candidatos  
- Votação  

#### 👨‍💼 Administrador
- Gerenciamento de candidatos  
- Envio de notificações  
- Controle do sistema  

---

### ⏱️ Controle de Votação

- Tempo limite definido pelo servidor  
- Encerramento automático  
- Apuração dos resultados  

---

### 📊 Resultados

- Total de votos por candidato  
- Percentual de votos  
- Identificação do vencedor  

---

## 🏗️ Arquitetura de Comunicação

### 🔌 TCP (Unicast)
- Login  
- Votação  
- Lista de candidatos  

### 📡 UDP (Multicast)
- Notificações em tempo real  
- Grupo: `224.1.1.1`  

---

## 🧵 Concorrência

- Servidor multi-threaded (`threading`)
- Uma thread por cliente  
- Processamento simultâneo  

---

## 🛠️ Representação de Dados

- Utilização de **JSON**
- Fácil leitura e extensibilidade

---

## 🧪 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|----------|--------|
| Python | Implementação geral |
| Socket (TCP/UDP) | Comunicação em rede |
| JSON | Serialização |
| Threading | Concorrência |

---

## 📌 Resultados Alcançados

- ✔️ Implementação completa das 5 questões  
- ✔️ Comunicação distribuída funcional  
- ✔️ Serialização manual eficiente  
- ✔️ Sistema concorrente robusto  
- ✔️ Integração TCP + UDP  

---

## 💡 Melhorias Futuras

- Interface Web (Flask ou Django)
- Persistência com banco de dados
- Autenticação de usuários
- Criptografia de comunicação
- Uso de gRPC ou Protocol Buffers

---

## 📚 Aprendizados

Este projeto consolidou conhecimentos em:

- Sistemas distribuídos  
- Comunicação em rede  
- Serialização de dados  
- Programação concorrente  

---

## 👨‍💻 Autor

Desenvolvido por **Avelino Facó** 

---

## ⭐ Destaque

Projeto ideal para demonstrar domínio em:

- Backend distribuído  
- Redes de computadores  
- Engenharia de software  
