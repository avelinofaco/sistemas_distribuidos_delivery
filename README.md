# 📡 Sistema Distribuído com Sockets, Streams e Votação de Delivery

---

## 🚀 Visão Geral

Este projeto apresenta a implementação de um **sistema distribuído completo**, desenvolvido para demonstrar na prática conceitos fundamentais de comunicação em rede, serialização de dados e concorrência.

A solução integra múltiplas tecnologias e paradigmas para simular um ambiente real de **votação de cardápio de delivery**, permitindo interação simultânea entre clientes e administradores.

---

## 🎯 Objetivos

- Implementar comunicação cliente-servidor via **Sockets (TCP/UDP)**
- Criar **streams personalizados** para manipulação de dados binários
- Aplicar **serialização manual** de objetos
- Construir um sistema distribuído com **concorrência**
- Simular um cenário real de aplicação (votação + pedidos)

---

## 🧩 Arquitetura do Sistema

O sistema foi dividido em três grandes módulos:

### 🔹 1. Sockets e Streams
Manipulação de dados em baixo nível utilizando `InputStream` e `OutputStream`.

### 🔹 2. Serialização
Empacotamento e transmissão de objetos (`Pedido`) via rede.

### 🔹 3. Sistema Distribuído de Votação
Aplicação prática utilizando TCP + UDP + Multithreading.

---

## 🧱 Modelagem de Dados (POJO)

As seguintes classes foram utilizadas:

- `Candidato` → itens disponíveis para votação  
- `Voto` → representa o voto do usuário  
- `ComandoAdmin` → ações administrativas  
- `Pedido` → base para serialização e streams  

---

## 🔄 Streams Personalizados

### 📤 PedidoOutputStream

Classe responsável por **serializar e enviar objetos `Pedido`** como fluxo de bytes.

**Funcionalidades:**
- Serialização manual de atributos
- Controle do tamanho dos dados enviados
- Suporte a múltiplos destinos

**Testes realizados:**
- Saída padrão (`System.out`)
- Arquivo (`FileOutputStream`)
- Socket TCP

---

### 📥 PedidoInputStream

Classe responsável por **ler e reconstruir objetos `Pedido`**.

**Funcionalidades:**
- Leitura de bytes
- Desserialização manual
- Reconstrução de objetos

**Testes realizados:**
- Entrada padrão (`System.in`)
- Arquivo (`FileInputStream`)
- Socket TCP

---

## 🔌 Comunicação Cliente-Servidor

### 🧠 Baseada na classe `Pedido` (Questão 4)

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

Para garantir robustez:

- **Header (4 bytes)** → tamanho da mensagem  
- **Payload** → dados serializados  

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

- Servidor multi-threaded  
- Uma thread por cliente  
- Processamento simultâneo de múltiplos usuários  

---

## 🛠️ Representação de Dados

- Utilização de **JSON**
- Alternativa ao Protocol Buffers
- Fácil leitura e extensibilidade

---

## 🧪 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|----------|--------|
| Java | Streams e serialização (`Pedido`) |
| Python | Comunicação via sockets |
| TCP | Comunicação confiável |
| UDP | Comunicação multicast |
| Threads | Concorrência |

---

## 📌 Resultados Alcançados

- ✔️ Implementação completa das 5 questões  
- ✔️ Streams personalizados funcionais  
- ✔️ Serialização manual eficiente  
- ✔️ Comunicação distribuída robusta  
- ✔️ Integração TCP + UDP  
- ✔️ Sistema escalável e concorrente  

---

## 💡 Melhorias Futuras

- Interface Web (React ou Flask)
- Persistência com banco de dados
- Autenticação de usuários
- Criptografia de comunicação
- Uso de Protocol Buffers ou gRPC

---

## 📚 Aprendizados

Este projeto consolidou conhecimentos em:

- Sistemas distribuídos  
- Comunicação em rede  
- Serialização de dados  
- Programação concorrente  
- Arquitetura de software  

---

## 👨‍💻 Autor

Desenvolvido por **Avelino Facó**  
📍 Ceará - Brasil  

---

## ⭐ Destaque

Projeto ideal para demonstrar domínio em:

- Backend distribuído  
- Redes de computadores  
- Engenharia de software  

---
