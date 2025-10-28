# 🏦 Banco SPX – Sistema Bancário em Python

Um **sistema bancário simples, desenvolvido para fins educacionais** desenvolvido em Python com base em **Programação Orientada a Objetos (POO)**, aplicando conceitos aprendidos em nossas aulas de BackEnd no Senai Jundiaí, com o tutor Carlos Ribeiro, sendo eles **abstração**, **herança**, **interfaces**, **encapsulamento**, **polimorfismo** e **relacionamentos entre classes** (associação, agregação e composição).

---

## 📚 Sumário do ReadMe

1. [🧠 Visão Geral do Projeto](#-visão-geral-do-projeto)
2. [🏗️ Arquitetura do Sistema](#️-arquitetura-do-sistema)
3. [💾 Classes e Responsabilidades](#-classes-e-responsabilidades)
4. [🔒 Visibilidade de Atributos e Métodos](#-visibilidade-de-atributos-e-métodos)
5. [🧩 Relacionamentos Entre Classes](#-relacionamentos-entre-classes)
6. [⚙️ Aplicação dos Conceitos de POO](#️-aplicação-dos-conceitos-de-poo)
7. [🖥️ Execução do Programa](#️-execução-do-programa)
8. [👨‍💻 Autores](#-autores)

---

## 🧠 Visão Geral do Projeto

O **Banco SPX** é um sistema bancário **digital e interativo** que permite:

- Cadastro e login de clientes;
- Criação automática de conta corrente;
- Conta corrente e Conta poupança disponíveis para uso do mesmo usuário;
- Diferentes regras sendo aplicadas para os diferentes tipos de conta;
- Depósitos, saques e transferências entre contas;
- Consulta de saldo e extrato detalhado;
- Edição de dados do cliente;
- Encerramento seguro da sessão e do programa.

O objetivo do projeto é **demonstrar a aplicação prática dos princípios da POO, como forma de avaliação final de BackEnd**, com uma estrutura modular e separação clara entre **entidades (classes)** e **funções de interface**.

---

## 🏗️ Arquitetura do Sistema

📂 **Projeto_Banco_SPX**  
│  
├── **main.py** – Arquivo principal que **controla o fluxo do programa** e inicializa o sistema.  
├── **functions.py** – Contém **funções auxiliares** e **menus interativos**, responsáveis pela interface textual.  
└── **classes.py** – Define as **classes principais** e **estrutura de POO**, como `Banco`, `Cliente` e `Conta`.

---

### 🔄 Fluxo geral:
1. O usuário inicia o programa (`main.py`).
2. O sistema exibe a **tela de boas-vindas** e o **menu de login**.
3. O cliente pode **cadastrar-se ou realizar login**.
4. Após logar, tem acesso ao **menu principal** com operações bancárias.
5. Todas as transações afetam o **objeto de conta** e são registradas no **extrato**.

---

## 💾 Classes e Responsabilidades

### 🏦 `class Banco`
- **Responsabilidade:** representar o banco em si e gerenciar seus clientes.
- **Atributos:**
  - `__nome`, `__localizacao`, `__agencia` → informações do banco.
  - `__clientes` → lista privada que armazena todos os clientes.
- **Métodos principais:**
  - `adicionar_cliente(cliente)` → adiciona um cliente ao banco.
  - Getters para acessar nome, agência e clientes.

🔹 *Encapsulamento forte* — todos os atributos são privados, garantindo segurança e controle sobre o acesso.

---

### 👤 `class Cliente`
- **Responsabilidade:** representar cada cliente do banco.
- **Atributos:**
  - `__nome`, `__cpf`, `__senha` → dados pessoais do cliente.
  - `__contas` → lista de contas do cliente.
- **Métodos principais:**
  - Getters e setters para nome, CPF e senha.
  - `adicionar_conta(conta)` → associa uma nova conta ao cliente.

🧩 *Associação* → o cliente **tem** contas bancárias, mas as contas também conhecem seu dono.

---

### 💸 `class Operacoes_Financeiras (ABC)`
- **Responsabilidade:** servir como **interface abstrata** que define o padrão das operações bancárias.
- **Métodos abstratos:**
  - `depositar(valor)`
  - `sacar(valor)`
  - `transferir(destino, valor)`

🔹 Garante que todas as classes de conta implementem esses métodos obrigatoriamente.

---

### 🧾 `class Conta (abstract)`
- **Responsabilidade:** representar uma conta genérica.
- **Atributos:**
  - `__id_conta` → identificador da conta.
  - `__cliente` → referência ao titular.
  - `_saldo` → saldo atual (protegido).
  - `__extrato` → objeto da classe `Extrato`.
- **Métodos principais:**
  - Getters de conta, cliente, saldo e extrato.
  - Representação textual (`__str__`) da conta.

🔹 *Composição* → a conta **contém** um objeto `Extrato`, que só existe enquanto a conta existir.

---

### 💳 `class Conta_Corrente (Conta)`
- **Responsabilidade:** implementar as operações da conta corrente.
- **Métodos:**
  - `depositar(valor)`
  - `sacar(valor)`
  - `transferir(conta_destino, valor)`

💡 Utiliza **polimorfismo** para implementar as operações financeiras conforme sua lógica própria.

---

### 💰 `class Conta_Poupanca (Conta)`
- **Responsabilidade:** versão da conta com **saldo mínimo para saque**.
- **Atributo adicional:**
  - `SaldoMinimoSaque = 100.0`
- **Métodos sobrescritos:**
  - `depositar`, `sacar` e `transferir` (com validações específicas).

🔒 Aplica **herança** e **polimorfismo**, alterando regras conforme o tipo de conta.

---

### 📄 `class Extrato`
- **Responsabilidade:** registrar e exibir todas as transações de uma conta.
- **Atributos:**
  - `__transacoes` → lista de tuplas com (data, descrição, valor).
- **Métodos:**
  - `adicionar_transacao(descricao, valor)`
  - `mostrar_extrato()`

🧩 *Composição* — o extrato pertence exclusivamente à conta que o criou.

---

## 🔒 Visibilidade de Atributos e Métodos

| Tipo | Símbolo | Exemplo | Acesso | Justificativa |
|------|----------|----------|---------|----------------|
| **Público** | — | `depositar()` | Livre | Métodos que precisam ser acessados fora da classe. |
| **Protegido** | `_` | `_saldo` | Subclasses | Permite herança sem quebrar encapsulamento total. |
| **Privado** | `__` | `__clientes`, `__senha` | Somente dentro da classe | Garante segurança e controle sobre dados sensíveis. |

➡️ **Motivo das escolhas:**  
A visibilidade foi definida conforme o **nível de sensibilidade** dos dados:
- Informações de **usuário e banco** → privadas (`__`) para evitar manipulação indevida.  
- Atributos como `_saldo` → protegidos (`_`) para permitir herança em `Conta_Corrente` e `Conta_Poupanca`.  
- Funções utilitárias (em `functions.py`) → públicas, pois precisam ser chamadas no fluxo principal.

---

## 🧩 Relacionamentos Entre Classes

| Tipo de Relacionamento | Exemplo | Descrição |
|------------------------|----------|------------|
| **Associação** | `Cliente → Conta` | Um cliente pode ter várias contas. |
| **Agregação** | `Banco → Clientes` | O banco agrega clientes, mas eles existem independentemente. |
| **Composição** | `Conta → Extrato` | O extrato é parte essencial da conta e deixa de existir sem ela. |

---

## ⚙️ Aplicação dos Conceitos de POO

| Conceito | Onde foi aplicado | Explicação |
|-----------|------------------|-------------|
| **Abstração** | `Operacoes_Financeiras` | Define uma interface genérica para operações bancárias. |
| **Encapsulamento** | Atributos privados (`__`) | Protege dados sensíveis e evita acessos diretos. |
| **Herança** | `Conta_Corrente` e `Conta_Poupanca` herdando de `Conta` | Reaproveitamento de código e especialização de comportamentos. |
| **Polimorfismo** | Métodos `depositar`, `sacar` e `transferir` | Sobrescritos com comportamentos diferentes conforme o tipo da conta. |

---

## 🖥️ Execução do Programa

### ▶️ Como rodar o projeto:
1. Certifique-se de ter o **Python 3.10+** instalado.
2. Baixe ou clone este repositório.
3. Execute no terminal:

```bash
python main.py
```

## 👨‍💻 Participantes do Projeto

- Matheus Kurachi
- Thiago Masseto
- Matheus Alves
- Lucas Silva
- Andre Nery
- Nicolas Bertacin

Desenvolvedores de Software em formação técnica pelo **Senai Jundiaí**, Instruídos por **Carlos Ribeiro ❤️**