# ---------------------------------------------------------------------------------------------------------------- #
# Arquivo para estrutura principal do projeto

from classes import *
from functions import * # Importar as funções auxiliares e as bibliotecas necessárias

banco = Banco("Banco SPX", "Jundiai-SP", "Agencia - 0001") # Instancia os atributos da classe Cliente

cliente_logado = False # garante que o usuario nunca comece logado no sistema

tela_inicio() # inicia a função de animação de inicio (tela de carregamento meramente ilustrativa)

# ---------------------------------------------------------------------------------------------------------------- #

while True: # inicia um loop controlado para forçar o usuario a realizar o login ou sair do software

    menu_login() # inicia a função que contem as informaçãoes base do login

    try: #Tratamento de erro caso o usuario adicione uma string no lugar do numero
        escolha_login = int(input("\nEscolha uma opção!!!\n-->")) # pede ao usuario que insira a opção que deseja, e armazena a resposta na variavel.
    except ValueError: # aqui é tratado o erro para o programa nao travaar
    
        limpar_terminal() # limpa o terminal
        print("Escolha Inválida!!!\nPor favor, atente-se em adicionar apenas números.") 
        espera_terminal() # pausa o terminal por 3 segundos

        continue # Volta para o começo do loop

    match escolha_login: # match case para prosseguir seguindo a escolha do usuario

        case 1: # case Realizar Login
            pass

        case 2: # case Cadastrar usuario
            pass
        
        case 3: # case para sair do software

            limpar_terminal() # limpa o terminal

            print("Encerrando o software... Até logo!") 

            espera_terminal() # pausa o terminal
            
            break # o break vai finalizar o software quebrando o loop do while True.

        case _: # case para opções invalidas

            limpar_terminal() # limpa o temrinal
            print("Opção inválida. Tente novamente!")
            espera_terminal() # pausa o terminal por 3 segundos

if cliente_logado == True: # antes de prosseguir para a proxima parte do software, é verificado se o usuario esta devidamente logado.
    while True: # inicia um loop controlado para garantir as funções principais do software para o usuario

        menu_principal() # inicia a funçãoq eu contem as informações basicas do menu principal

        try:    # Tratamento de erro, caso o usuário adicione uma string no lugar do numero inteiro.
            escolha_usuario = int(input("\nEscolha uma opção!\n->")) # armazena a escolha do usuario na variavel escolha_usuario
        except ValueError: # aqui tratamos esse erro para o programa não travar
            
            limpar_terminal() # limpa o temrinal
            print("Escolha Inválida!!!\nPor favor, atente-se em adicionar apenas números.")
            espera_terminal() # pausa o temrinal por 3 segundos

            continue # volta para o começo de loop do while True

        match escolha_usuario: # match case para prosseguir com a escolha do usuario
            
            case 1: # case Realizar saque
                
                limpar_terminal()
                print("Você escolheu: Realizar saque")
                espera_terminal()
                
            case 2: # case Realizar deposito
                
                limpar_terminal()
                print("Você escolheu: Realizar depósito")
                espera_terminal()

            case 3: # case Consultar saldo
                
                limpar_terminal()
                print("Você escolheu: Consultar saldo")
                espera_terminal()

            case 4: # case Consultar extrato
                
                limpar_terminal()
                print("Você escolheu: Consultar extrato")
                espera_terminal()

            case 5: # case Alterar as informações da conta
                
                limpar_terminal()
                print("Você escolheu: Alterar informações da conta")
                espera_terminal()

            case 6: # case Sair da conta
                
                limpar_terminal()
                print("Saindo da conta...")
                espera_terminal()

            case 7: # case Finalizar o software

                limpar_terminal()
                print("Encerrando o software... Até logo!")
                espera_terminal()

                break # o break vai finalizar o software quebrando o loop do while True.


            case _: # case para opções invalidas

                limpar_terminal()
                print("Opção inválida. Tente novamente!")
                espera_terminal()

# ---------------------------------------------------------------------------------------------------------------- #

