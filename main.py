# Arquivo para estrutura principal do projeto

from functions import * # Importar as funções auxiliares e as bibliotecas necessárias


while True:

    menu_principal()

    try:    # Tratamento de erro, caso o usuário adicione uma string no lugar do numero inteiro.
        escolha_usuario = int(input("\nEscolha uma opção!\n->"))
    except ValueError: # aqui tratamos esse erro para o programa não travar
        
        limpar_terminal()
        print("Escolha Inválida!!!\n Por favor, atente-se em adicionar apenas números.")
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

            limpar_terminal()
            break # o break vai finalizar o software quebrando o loop do while True.

        case _:

            limpar_terminal()
            print("Opção inválida. Tente novamente!")
            espera_terminal()

