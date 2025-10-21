# ---------------------------------------------------------------------------------------------------------------- #
# Arquivo para estrutura principal do projeto

from classes import *
from functions import * # Importar as funções auxiliares e as bibliotecas necessárias

banco = Banco("Banco SPX", "Jundiai-SP", "Agencia - 0001")

cliente_logado = False

tela_inicio()

# ---------------------------------------------------------------------------------------------------------------- #

while True:

    menu_login()

    try: #Tratamento de erro caso o usuario adicione uma string no lugar do numero
        escolha_login = int(input("\nEscolha uma opção!!!\n-->"))
    except ValueError: # aqui é tratado o erro para o programa nao travaar
    
        limpar_terminal()
        print("Escolha Inválida!!!\nPor favor, atente-se em adicionar apenas números.")
        espera_terminal()

        continue # Volta para o começo do loop

    match escolha_login:

        case 1:
            # Realizar login
            pass
        case 2: 
            # Cadastrar Login 
            pass
        case 3:
            # Sair do software

            limpar_terminal()

            print("Encerrando o software... Até logo!") 

            espera_terminal()
            
            break # o break vai finalizar o software quebrando o loop do while True.

        case _:
            limpar_terminal()
            print("Opção inválida. Tente novamente!")
            espera_terminal()

if cliente_logado == True:
    while True:

        menu_principal()

        try:    # Tratamento de erro, caso o usuário adicione uma string no lugar do numero inteiro.
            escolha_usuario = int(input("\nEscolha uma opção!\n->"))
        except ValueError: # aqui tratamos esse erro para o programa não travar
            
            limpar_terminal()
            print("Escolha Inválida!!!\nPor favor, atente-se em adicionar apenas números.")
            espera_terminal()

            continue # volta para o começo de loop do while True

        match escolha_usuario:
            
            case 1:
                
                limpar_terminal()
                print("Você escolheu: Realizar saque")
                espera_terminal()
                
            case 2:
                
                limpar_terminal()
                print("Você escolheu: Realizar depósito")
                espera_terminal()

            case 3:
                
                limpar_terminal()
                print("Você escolheu: Consultar saldo")
                espera_terminal()

            case 4:
                
                limpar_terminal()
                print("Você escolheu: Consultar extrato")
                espera_terminal()

            case 5:
                
                limpar_terminal()
                print("Você escolheu: Alterar informações da conta")
                espera_terminal()

            case 6:

                limpar_terminal()
                print("Saindo da conta...")
                espera_terminal()

            case 7:

                limpar_terminal()
                print("Encerrando o software... Até logo!")
                espera_terminal()

                break # o break vai finalizar o software quebrando o loop do while True.


            case _:

                limpar_terminal()
                print("Opção inválida. Tente novamente!")
                espera_terminal()

# ---------------------------------------------------------------------------------------------------------------- #

