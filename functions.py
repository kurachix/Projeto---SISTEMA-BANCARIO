# Arquivo para armazenar funções auxiliares do projeto

from classes import * # importa todas as classes para o arquivo de funções 
import time # importa a bibliotaca time, para adicionar pausar ao longo do codigo
import os # importa a  biblioteca os, para limpar o terminal e pausa-lo ao longo do codigo

# ---------------------------------------------------------------------------------------------------------------- #

def limpar_terminal(): # Função para limpar o terminal
    
    os.system("cls") # comando que limpa o terminal

def espera_terminal(): # Função para deixar uma espera de 3 segundos no terminal, usando a biblioteca time

    time.sleep(3) # comando que pausa o terminal pelo tempo de 3 segundos

# ---------------------------------------------------------------------------------------------------------------- #

# Função para cadastrar cliente
def cadastrar_cliente(Banco):

    def aceitar_termos(): # funçãoo que contem as informações base para a aceitação de termos.
        limpar_terminal() # limpa o terminal

        print(50 * "-") # varios traços em seguida um do outro, servem para deixar o terminal estetica
        print("Antes, confirme os termos de uso do Banco SPX!".center(50)) # center(50) para deixar o texto no centro de 50 caracteres
        print(50 * "-") # varios traços em seguida um do outro, servem para deixar o terminal estetica

        print("\n1- Aceitar os Termos\n2- Rejeitar os Termos\n3-Ler os termos")
        escolha = int(input("\n--> ")) # variavel que vai armazenar a escolha do usuario
        
        return escolha # vai retornar a variavel escolha para fora da função.
    
    while True: # inicia um loop controlado para garantir que o usuario aceite os termos ou saia do software.
        limpar_terminal() # função que limpa o terminal
        print("Precisaremos de algumas informações pessoais para prosseguir com a criação da conta!!")
        
        escolha_termos_de_servico = aceitar_termos() 

        match escolha_termos_de_servico: # match case para prosseguir com a escolha do usuario

            case 1:  # case Aceitar os termos
                break  # Sai do loop e prossegue com cadastro

            case 2:  # case Rejeitar os termos
                limpar_terminal() # função que limpa o terminal
                print("Infelizmente, ao não aceitar os termos de uso, não é possível criar uma conta no Banco SPX")
                espera_terminal() # função que pausa o terminal por 3 segundos
                return  # Sai da função

            case 3:  #  case Exibir o termo de uso para o usuario
                limpar_terminal() # função limpar o terminal
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
                espera_terminal() # função que pausa o terminal por 3 segundos
                # Loop volta e pede novamente para aceitar/rejeitar

    # Cadastro do cliente
    nome = input("Nome: ") # armazena o nome do usuario na variavel
    cpf = input("CPF: ") # armazena o cpf do usuario na variavel
    senha = input("Senha: ") # armazrna a senha do usuario na variavel
    Banco.cadastrar_cliente(nome, cpf, senha) # ativa a função do metodo cadastrar_cliente, passando os dados das variaveis.



def login_cliente(): # define a função login_cliente

    limpar_terminal() # fiunção limpa o terminal
    
    print( 50 * "-") # varios traços em seguida um do outro, servem para deixar o terminal estetica
    print("Realize seu Login para prosseguir!!!".center(50))
    print( 50 * "-") # varios traços em seguida um do outro, servem para deixar o terminal estetica

    cpf = input("CPF: ") # armazena a variavel cpf
    senha = input("Senha: ") # amazena a variavel senha

    return Banco.login(cpf, senha) # ativa e retorna a função login, passando as variaveis cpf e senha.

# ---------------------------------------------------------------------------------------------------------------- #


def tela_inicio(): # define a função tela_inicio

    limpar_terminal()

        # Cabeçalho do banco
    print("="*50) # varios sinais de igual em seguida um do outro, servem para deixar o terminal estetica
    print("BANCO SPX".center(50))
    print("="*50) # varios sinais de igual em seguida um do outro, servem para deixar o terminal estetica
    print("\nBem-vindo ao Banco SPX!")
    print("O seu banco digital de confiança.\n")
    
    # animação de carregamento
    # Exibe a palavra "Carregando" na tela sem pular linha
    print("Carregando", end="")

    # Inicia um loop que vai repetir 9 vezes (para mostrar 9 pontinhos)
    for _ in range(9):
        # Exibe um ponto sem quebrar a linha, simulando um "carregando..."
        # O parâmetro flush=True força o print a aparecer imediatamente na tela
        print(".", end="", flush=True)
        # Faz o programa esperar 0,5 segundos antes de mostrar o próximo ponto
        time.sleep(0.5)

    # Depois que o loop termina, pula uma linha para deixar a saída organizada
    print("\n")


def menu_principal(): # Função que contêm o conteudo básico do menu


    limpar_terminal() # função que limpa o terminal

    print( 30 * "-" ) # varios traços em seguida um do outro, servem para deixar o terminal estetica
    print("Seja bem-vindo ao Banco SPX".center(30)) # o center serve para alinhar dentro da quantidade de caracteres passadas
    print("O que você deseja hoje?".center(30)) # o center serve para alinhar dentro da quantidade de caracteres passadas
    print( 30 * "-" ) # varios traços em seguida um do outro, servem para deixar o terminal estetica

    print("\n1 - Realizar saque")
    print("2 - Realizar depósito")
    print("3 - Consular saldo")
    print("4 - Consultar extrato")
    print("5 - Alterar informações da conta")
    print("6 - Sair da conta")
    print("7 - Sair do software")

    print("")
    print( 30 * "-" ) # varios traços em seguida um do outro, servem para deixar o terminal estetica

def menu_login(): # Função que contêm o conteudo basico de login

    limpar_terminal() # função que limpa o terminal

    print( 30 * "-" ) # varios traços em seguida um do outro, servem para deixar o terminal estetica
    print("Seja bem-vindo ao Banco SPX".center(30)) # o center serve para alinhar dentro da quantidade de caracteres passadas
    print("Realize o login para prosseguir".center(30)) # o center serve para alinhar dentro da quantidade de caracteres passadas
    print( 30 * "-" ) # varios traços em seguida um do outro, servem para deixar o terminal estetica

    print("\n1 - Realizar Login")
    print("2 - Realizar cadastro")
    print("3- Sair do software")

    print("")
    print( 30 * "-" ) # varios traços em seguida um do outro, servem para deixar o terminal estetica






