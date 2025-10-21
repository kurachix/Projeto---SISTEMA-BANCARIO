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

# codigo temporario ate deciderem de qual esta melhor
# Classes que gerencia clientes de uma agência: adiciona e lista clientes e fornece getters para nome, localização e número da agência.
def adicionar_cliente(self, cliente):
        self.__clientes.append(cliente)
    
    def listar_clientes(self):
        return self.__clientes
    
    def get_nome(self):
        return self.__nome
    
    def get_localizacao(self):
        return self.__localizacao
    
    def get_agencia(self):
        return self.__agencia
# |--------------------------------------------------------------------------------------------------------------------|
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

