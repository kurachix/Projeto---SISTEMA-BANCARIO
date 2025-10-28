# ---------------------------------------------------------------------------------------------------------------- #
# Arquivo para estrutura principal do projeto

from classes import *  # importa todas as classes para a main
from functions import *  # Importa as funções auxiliares e as bibliotecas necessárias

banco = Banco("Banco SPX", "Jundiaí-SP", "Agência - 0001")  # Instancia o banco

cliente_logado = None  # guarda o cliente logado (None = nenhum cliente logado)

tela_inicio()  # inicia a função de animação de início (tela de carregamento meramente ilustrativa)

# ---------------------------------------------------------------------------------------------------------------- #

while True:  # inicia um loop controlado para forçar o usuário a realizar o login ou sair do software

    menu_login()  # inicia a função que contém as informações base do login

    try:  # Tratamento de erro caso o usuário adicione uma string no lugar do número
        escolha_login = int(input("\nEscolha uma opção!!!\n--> "))
    except ValueError:  # aqui é tratado o erro para o programa não travar
        limpar_terminal()
        print("Escolha Inválida!!!\nPor favor, atente-se em adicionar apenas números.")
        espera_terminal()
        continue  # Volta para o começo do loop

    match escolha_login:

        case 1:  # Realizar Login
            cliente_logado = login_cliente(banco)
            if cliente_logado:
                break  # Sai do loop de login e vai para o menu principal

        case 2:  # Cadastrar usuário
            cadastrar_cliente(banco)

        case 3:  # Sair do software
            limpar_terminal()
            print("Encerrando o software... Até logo!")
            espera_terminal()
            exit()  # Finaliza o programa completamente

        case _:  # Opções inválidas
            limpar_terminal()
            print("Opção inválida. Tente novamente!")
            espera_terminal()

# ---------------------------------------------------------------------------------------------------------------- #

if cliente_logado:  # verifica se há um cliente logado
    while True:  # inicia um loop controlado para garantir as funções principais do software para o usuário

        menu_principal()  # inicia a função que contém as informações básicas do menu principal

        try:  # Tratamento de erro, caso o usuário adicione uma string no lugar do número inteiro
            escolha_usuario = int(input("\nEscolha uma opção!\n-> "))
        except ValueError:
            limpar_terminal()
            print("Escolha Inválida!!!\nPor favor, atente-se em adicionar apenas números.")
            espera_terminal()
            continue

        match escolha_usuario:

            case 1:  # Realizar saque
                limpar_terminal()
                print("Você escolheu: Realizar saque")
                espera_terminal()

            case 2:  # Realizar depósito
                limpar_terminal()
                print("Você escolheu: Realizar depósito")
                espera_terminal()

            case 3:  # Consultar saldo
                limpar_terminal()
                print("Você escolheu: Consultar saldo")
                espera_terminal()

            case 4:  # Consultar extrato
                limpar_terminal()
                print("Você escolheu: Consultar extrato")
                espera_terminal()

            case 5:  # Alterar as informações da conta
                limpar_terminal()
                print("Você escolheu: Alterar informações da conta")
                espera_terminal()

            case 6:  # Sair da conta
                limpar_terminal()
                print("Saindo da conta...")
                espera_terminal()
                cliente_logado = None
                break  # sai do menu principal e volta ao menu de login

            case 7:  # Finalizar o software
                limpar_terminal()
                print("Encerrando o software... Até logo!")
                espera_terminal()
                exit()

            case _:  # Opções inválidas
                limpar_terminal()
                print("Opção inválida. Tente novamente!")
                espera_terminal()



