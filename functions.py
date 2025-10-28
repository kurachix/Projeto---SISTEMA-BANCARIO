# Arquivo para armazenar funções auxiliares do projeto

from classes import *  # importa todas as classes
import time
import os

# ---------------------------------------------------------------------------------------------------------------- #
# Funções utilitárias

def limpar_terminal():
    """Limpa o terminal"""
    os.system("cls")


def espera_terminal():
    """Pausa o terminal por 3 segundos"""
    time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------- #
# Funções principais do sistema

def cadastrar_cliente(banco: Banco):
    """Função para cadastrar um novo cliente"""

    # ... (a parte dos termos de uso e dados pessoais permanece igual)

    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    senha = input("Senha: ").strip()

    cliente_existente = None
    for cliente in banco.get_clientes():
        if cliente.getCpf() == cpf:
            cliente_existente = cliente
            break

    # Escolha do tipo de conta
    limpar_terminal()
    print("Escolha o tipo de conta que deseja criar:\n")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")

    while True:
        try:
            tipo = int(input("\n--> "))
            if tipo in (1, 2):
                break
            else:
                print("Opção inválida! Digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    tipo_conta = "corrente" if tipo == 1 else "poupanca"
    prefixo = "CC" if tipo == 1 else "CP"
    id_conta = f"{prefixo}-{len(banco.get_clientes()) + 1}"

    # Se o cliente já existe, só adiciona uma nova conta
    if cliente_existente:
        limpar_terminal()
        print(f"O cliente {cliente_existente.getNome()} já possui cadastro.")
        print("Adicionando nova conta ao perfil existente...\n")

        if tipo == 1:
            nova_conta = Conta_Corrente(id_conta, cliente_existente)
        else:
            nova_conta = Conta_Poupanca(id_conta, cliente_existente)

        cliente_existente.adicionar_conta(nova_conta)
        print(f"✅ Nova conta {tipo_conta.title()} criada: {nova_conta.getIdConta()}")
        espera_terminal()
        return

    # Se não existe, cria um novo cliente normalmente
    novo_cliente = Cliente(nome, cpf, senha)

    if tipo == 1:
        nova_conta = Conta_Corrente(id_conta, novo_cliente)
    else:
        nova_conta = Conta_Poupanca(id_conta, novo_cliente)

    novo_cliente.adicionar_conta(nova_conta)
    banco.adicionar_cliente(novo_cliente)

    limpar_terminal()
    print(f"✅ Cliente {nome} cadastrado com sucesso!")
    print(f"🏦 Conta {tipo_conta.title()} criada automaticamente: {nova_conta.getIdConta()}")
    espera_terminal()




# ---------------------------------------------------------------------------------------------------------------- #

def login_cliente(banco: Banco):
    """Função para login do cliente"""

    limpar_terminal()
    print("=== LOGIN ===\n")

    cpf = input("Digite seu CPF: ").strip()
    senha = input("Digite sua senha: ").strip()

    # Procura cliente
    cliente_logado = None
    for cliente in banco.get_clientes():
        if cliente.getCpf() == cpf and cliente.getSenha() == senha:
            cliente_logado = cliente
            break

    if not cliente_logado:
        limpar_terminal()
        print("CPF ou senha incorretos!")
        espera_terminal()
        return None

    # Se o cliente tem mais de uma conta, pergunta qual ele quer acessar
    contas = cliente_logado._Cliente__contas
    if len(contas) > 1:
        limpar_terminal()
        print(f"Bem-vindo de volta, {cliente_logado.getNome()}!\n")
        print("Você possui mais de uma conta. Escolha qual deseja acessar:\n")

        for i, conta in enumerate(contas, start=1):
            tipo = "Conta Corrente" if "CC" in conta.getIdConta() else "Conta Poupança"
            print(f"{i} - {tipo} ({conta.getIdConta()})")

        while True:
            try:
                escolha = int(input("\n--> "))
                if 1 <= escolha <= len(contas):
                    conta_escolhida = contas[escolha - 1]
                    limpar_terminal()
                    print(f"Acessando {conta_escolhida.getIdConta()}...\n")
                    espera_terminal()
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
    else:
        conta_escolhida = contas[0]

    # Armazena qual conta o cliente escolheu (útil para o menu principal)
    cliente_logado.conta_ativa = conta_escolhida

    limpar_terminal()
    print(f"✅ Login realizado com sucesso! Bem-vindo(a), {cliente_logado.getNome()}!")
    espera_terminal()
    return cliente_logado

# ---------------------------------------------------------------------------------------------------------------- #
# Telas e Menus

def tela_inicio():
    """Tela inicial ilustrativa"""
    limpar_terminal()
    print("=" * 50)
    print("BANCO SPX".center(50))
    print("=" * 50)
    print("\nBem-vindo ao Banco SPX!")
    print("O seu banco digital de confiança.\n")

    print("Carregando", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n")

# ---------------------------------------------------------------------------------------------------------------- #

def menu_principal():
    """Menu principal após o login"""
    limpar_terminal()
    print(30 * "-")
    print("Seja bem-vindo ao Banco SPX".center(30))
    print("O que você deseja hoje?".center(30))
    print(30 * "-")

    print("\n1 - Realizar saque")
    print("2 - Realizar depósito")
    print("3 - Consultar saldo")
    print("4 - Consultar extrato")
    print("5 - Alterar informações da conta")
    print("6 - Sair da conta")
    print("7 - Finalizar o software")
    print("8 - Transferencia")

    print("\n" + 30 * "-")

# ---------------------------------------------------------------------------------------------------------------- #

def menu_login():
    """Menu de login principal"""
    limpar_terminal()
    print(30 * "-")
    print("Seja bem-vindo ao Banco SPX".center(30))
    print("Realize o login para prosseguir".center(30))
    print(30 * "-")

    print("\n1 - Realizar Login")
    print("2 - Realizar Cadastro")
    print("3 - Sair do Software")

    print("\n" + 30 * "-")
