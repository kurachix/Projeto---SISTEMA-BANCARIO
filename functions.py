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

    def aceitar_termos():
        limpar_terminal()
        print(50 * "-")
        print("Antes, confirme os termos de uso do Banco SPX!".center(50))
        print(50 * "-")

        print("\n1 - Aceitar os Termos\n2 - Rejeitar os Termos\n3 - Ler os Termos")
        try:
            escolha = int(input("\n--> "))
        except ValueError:
            limpar_terminal()
            print("Entrada inválida! Digite apenas números.")
            espera_terminal()
            return aceitar_termos()

        return escolha

    # --------------------------- TERMOS DE USO --------------------------- #
    while True:
        limpar_terminal()
        print("Precisaremos de algumas informações pessoais para prosseguir com a criação da conta!!")

        escolha_termos_de_servico = aceitar_termos()

        match escolha_termos_de_servico:
            case 1:  # Aceitou os termos
                break
            case 2:  # Rejeitou
                limpar_terminal()
                print("Infelizmente, ao não aceitar os termos de uso, não é possível criar uma conta no Banco SPX.")
                espera_terminal()
                return
            case 3:  # Leu os termos
                limpar_terminal()
                print("""
=========================
        TERMOS DE USO
=========================
- O banco não se responsabiliza por erros de terceiros.
- Mantenha sua senha em segurança.
- Não compartilhe sua conta com terceiros.
- O sistema não se responsabiliza por perdas reais.
- Ao continuar, você concorda com estes termos.
=========================
                """)
                espera_terminal()
            case _:  # Opção inválida
                limpar_terminal()
                print("Opção inválida. Tente novamente!")
                espera_terminal()

    # --------------------------- DADOS DO CLIENTE --------------------------- #
    limpar_terminal()
    print("Informe seus dados de cadastro abaixo:\n")

    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    senha = input("Senha: ").strip()  # .strip() remove espaços em branco

    # Verifica se já existe cliente com esse CPF
    for cliente in banco.get_clientes():
        if cliente.getCpf() == cpf:
            limpar_terminal()
            print("Já existe um cliente cadastrado com esse CPF!")
            espera_terminal()
            return

    # --------------------------- TIPO DE CONTA --------------------------- #
    limpar_terminal()
    print("=== ESCOLHA O TIPO DE CONTA ===")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")

    tipo_conta = None
    while tipo_conta not in (1, 2):
        try:
            tipo_conta = int(input("\nDigite o número da opção desejada: "))
            if tipo_conta not in (1, 2):
                print("Opção inválida! Escolha 1 ou 2.")
        except ValueError:
            print("Digite apenas números!")

    # Cria o cliente e adiciona ao banco
    novo_cliente = Cliente(nome, cpf, senha)

    if tipo_conta == 1:
        nova_conta = Conta_Corrente(f"CC-{len(banco.get_clientes()) + 1}", novo_cliente)
        tipo_nome = "Conta Corrente"
    else:
        nova_conta = Conta_Poupanca(f"CP-{len(banco.get_clientes()) + 1}", novo_cliente)
        tipo_nome = "Conta Poupança"

    novo_cliente.adicionar_conta(nova_conta)
    banco.adicionar_cliente(novo_cliente)

    # --------------------------- FINALIZAÇÃO --------------------------- #
    limpar_terminal()
    print("=========================================")
    print(f"🎉 Cliente {nome} cadastrado com sucesso! 🎉")
    print(f"Tipo de conta: {tipo_nome}")
    print(f"Número da conta: {nova_conta.getIdConta()}")
    print("=========================================")
    espera_terminal()


# ---------------------------------------------------------------------------------------------------------------- #

def login_cliente(banco: Banco):
    """Função para realizar o login de um cliente"""
    limpar_terminal()
    print("=== LOGIN ===\n")
    cpf = input("CPF: ").strip() #.strip retirar os espaços em branco
    senha = input("Senha: ").strip()

    # Verifica nos clientes do banco
    for cliente in banco.get_clientes():
        if cliente.getCpf() == cpf and cliente.getSenha() == senha:
            limpar_terminal()
            print(f"Bem-vindo de volta, {cliente.getNome()}!")
            espera_terminal()
            return cliente

    limpar_terminal()
    print(" CPF ou senha incorretos.")
    espera_terminal()
    return None

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
