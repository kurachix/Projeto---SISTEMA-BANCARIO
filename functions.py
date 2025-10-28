# Arquivo para armazenar funções auxiliares do projeto

from classes import *  # importa todas as classes para o arquivo de funções 
import time  # importa a biblioteca time, para adicionar pausas ao longo do código
import os  # importa a biblioteca os, para limpar o terminal e pausá-lo ao longo do código

# ---------------------------------------------------------------------------------------------------------------- #

def limpar_terminal():  # Função para limpar o terminal
    os.system("cls")  # comando que limpa o terminal

def espera_terminal():  # Função para deixar uma espera de 3 segundos no terminal, usando a biblioteca time
    time.sleep(3)  # comando que pausa o terminal pelo tempo de 3 segundos

# ---------------------------------------------------------------------------------------------------------------- #

# Função para cadastrar cliente
def cadastrar_cliente(Banco):

    def aceitar_termos():  # função que contém as informações base para a aceitação de termos.
        limpar_terminal()  # limpa o terminal

        print(50 * "-")
        print("Antes, confirme os termos de uso do Banco SPX!".center(50))
        print(50 * "-")

        print("\n1- Aceitar os Termos\n2- Rejeitar os Termos\n3-Ler os termos")
        escolha = int(input("\n--> "))
        return escolha

    while True:  # inicia um loop controlado para garantir que o usuário aceite os termos ou saia do software.
        limpar_terminal()
        print("Precisaremos de algumas informações pessoais para prosseguir com a criação da conta!!")

        escolha_termos_de_servico = aceitar_termos()

        match escolha_termos_de_servico:
            case 1:
                break  # Sai do loop e prossegue com cadastro

            case 2:
                limpar_terminal()
                print("Infelizmente, ao não aceitar os termos de uso, não é possível criar uma conta no Banco SPX")
                espera_terminal()
                return  # Sai da função

            case 3:
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

    # Cadastro do cliente
    nome = input("Nome: ")
    cpf = input("CPF: ")
    senha = input("Senha: ")

    novo_cliente = Cliente(nome, cpf, senha)
    Banco.adicionar_cliente(novo_cliente)

    limpar_terminal()
    print("Cadastro realizado com sucesso!")
    espera_terminal()


def login_cliente(Banco):  # define a função login_cliente
    limpar_terminal()

    print(50 * "-")
    print("Realize seu Login para prosseguir!!!".center(50))
    print(50 * "-")

    cpf = input("CPF: ")
    senha = input("Senha: ")

    for cliente in Banco.get_clientes():
        if cliente.getCpf() == cpf and cliente.getSenha() == senha:
            print("Login realizado com sucesso!")
            espera_terminal()
            return cliente

    print("CPF ou senha incorretos.")
    espera_terminal()
    
    return cliente_logado == True

# ---------------------------------------------------------------------------------------------------------------- #

def tela_inicio():  # define a função tela_inicio
    limpar_terminal()

    # Cabeçalho do banco
    print("=" * 50)
    print("BANCO SPX".center(50))
    print("=" * 50)
    print("\nBem-vindo ao Banco SPX!")
    print("O seu banco digital de confiança.\n")

    # animação de carregamento
    print("Carregando", end="")

    for _ in range(9):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print("\n")


def menu_principal():  # Função que contém o conteúdo básico do menu
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
    print("7 - Sair do software")

    print("")
    print(30 * "-")


def menu_login():  # Função que contém o conteúdo básico de login
    limpar_terminal()

    print(30 * "-")
    print("Seja bem-vindo ao Banco SPX".center(30))
    print("Realize o login para prosseguir".center(30))
    print(30 * "-")

    print("\n1 - Realizar Login")
    print("2 - Realizar cadastro")
    print("3 - Sair do software")

    print("")
    print(30 * "-")







