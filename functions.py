# Arquivo para armazenar funções auxiliares do projeto

from abc import ABC, abstractmethod
import time
import os

def limpar_terminal(): # Função para limpar o terminal
    
    os.system("cls")

def espera_terminal(): # Função para deixar uma espera de 3 segundos no terminal, usando a biblioteca time()

    time.sleep(3)


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




