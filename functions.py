# Arquivo para armazenar funções auxiliares do projeto

import os

def limpar_terminal(): # Função para limpar o terminal
    
    os.system("cls")


def menu_principal():

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
    

