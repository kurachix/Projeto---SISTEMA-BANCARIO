# Arquivo para estrutura principal do projeto

from functions import * # Importar as funções auxiliares e as bibliotecas necessárias


while True:

    menu_principal()

    escolha_usuario = int(input("\nEscolha uma opção!\n->"))

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
            break

        case _:

            limpar_terminal()
            print("Opção inválida. Tente novamente!")
            espera_terminal()

