# Arquivo para armazenar as classes do projeto

from abc import ABC, abstractmethod

# Classe que representa o banco 
class Banco:
    
    def __init__(self, nome, localizacao, agencia):
        # Atributos principais do banco
        self.__nome = nome
        self.__localizacao = localizacao
        self.__agencia = agencia

        # Lista que armazena todos os clientes cadastrados
        self.__clientes = []

        # Metódos Getters

    def get_nome(self):
        # retorna o nome do banco
        return self.__nome

    def get_localizacao(self):
        # retonra a localização do banco
        return self.__localizacao

    def get_agencia(self):
        # retorna o numero da agencia
        return self.__agencia

    def get_clientes(self):
        # retorna a lista de clientes
        return self.__clientes

class Cliente: # Classe pasa gerenciar as ações do cliente
    pass

class Operacoes_Financeiras: # Interface de padronização para operações financeiras
    pass

class Conta: # Classe abstrata para gerenciar a conta corrente e poupança
    pass

class Conta_Corrente(Conta, Operacoes_Financeiras): # Conta corrente que herda de Conta e Operacoes_Financeiras
    pass

class Conta_Poupanca(Conta, Operacoes_Financeiras): # Conta corrente que herda de Conta e Operacoes_Financeiras
    pass

class Extrato: # classe que "cuidara" do extrato
    pass

