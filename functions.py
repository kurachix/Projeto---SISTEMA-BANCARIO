# Arquivo para armazenar funções auxiliares do projeto

from classes import *
import time
import os

# ---------------------------------------------------------------------------------------------------------------- #

def limpar_terminal(): # Função para limpar o terminal
    
    os.system("cls")

def espera_terminal(): # Função para deixar uma espera de 3 segundos no terminal, usando a biblioteca time()

    time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------- #

# Função para cadastrar cliente
def cadastrar_cliente(Banco):

    def aceitar_termos():
        limpar_terminal()

        print(50 * "-")
        print("Antes, confirme os termos de uso do Banco SPX!".center(50))
        print(50 * "-")

        print("\n1- Aceitar os Termos\n2- Rejeitar os Termos\n3-Ler os termos")
        escolha = int(input("\n--> "))
        return escolha
    
    while True:
        limpar_terminal()
        print("Precisaremos de algumas informações pessoais para prosseguir com a criação da conta!!")
        
        escolha_termos_de_servico = aceitar_termos()

        match escolha_termos_de_servico:

            case 1:  # Aceitar
                break  # Sai do loop e prossegue com cadastro

            case 2:  # Rejeitar
                limpar_terminal()
                print("Infelizmente, ao não aceitar os termos de uso, não é possível criar uma conta no Banco SPX")
                espera_terminal()
                return  # Sai da função

            case 3:  # Ler termos
                limpar_terminal()
                print("""
                =========================
                    TERMOS DE USO
                =========================
                - O banco não se responsabiliza por erros terceiros.
                - Mantenha sua senha em segurança.
                - Não compartilhe sua conta com terceiros.
                - O sistema não se responsabiliza por perdas reais.
                - Ao continuar, você concorda com estes termos.
                =========================
                """)
                espera_terminal()
                # Loop volta e pede novamente para aceitar/rejeitar

    # Cadastro do cliente
    nome = input("Nome: ")
    cpf = input("CPF: ")
    senha = input("Senha: ")
    Banco.cadastrar_cliente(nome, cpf, senha)



def login_cliente():

    limpar_terminal()
    
    print( 50 * "-")
    print("Realize seu Login para prosseguir!!!".center(50))
    print( 50 * "-")

    cpf = input("CPF: ")
    senha = input("Senha: ")

    return Banco.login(cpf, senha)

# ---------------------------------------------------------------------------------------------------------------- #

def menu_principal(): # Função que contêm o conteudo básico do menu


    limpar_terminal()

    print( 30 * "-" )
    print("Seja bem-vindo ao Banco SPX".center(30))
    print("O que você deseja hoje?".center(30))
    print( 30 * "-" )

    print("\n1 - Realizar saque")
    print("2 - Realizar depósito")
    print("3 - Consular saldo")
    print("4 - Consultar extrato")
    print("5 - Alterar informações da conta")
    print("6 - Sair da conta")
    print("7 - Sair do software")

    print("")
    print( 30 * "-" )

def menu_login(): # Função que contêm o conteudo basico de login

    limpar_terminal()

    print( 30 * "-" )
    print("Seja bem-vindo ao Banco SPX".center(30))
    print("Realize o login para prosseguir".center(30))
    print( 30 * "-" )

    print("\n1 - Realizar Login")
    print("2 - Realizar cadastro")

    print("")
    print( 30 * "-" )






