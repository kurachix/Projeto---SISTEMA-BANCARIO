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
    
        # Métodos principais

    def adicionar_cliente(self, cliente):
        self.__clientes.append(cliente)

class Cliente: # Classe pasa gerenciar as ações do cliente
    def __init__(self, nome : str, cpf : str, senha : str):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def getNome(self):
        return self.__nome
    def getCpf(self):
        return self.__cpf
    def getSenha(self):
        return self.__senha
    
    def setNome(self, nome):
        self.__nome = nome
    def setCpf(self,cpf):
        self.__cpf = cpf
    def setSenha(self, senha):
        self.__senha = senha 


class Operacoes_Financeiras(ABC): # Interface de padronização para operações financeiras

    @abstractmethod
    def depositar(self, valor:float):
        pass

    @abstractmethod
    def sacar(self, valor:float):
        pass

    @abstractmethod
    def transferencia(self, destino, valor:float):
        pass
    

class Conta: # Classe abstrata para gerenciar a conta corrente e poupança
    def __init__(self, id_cliente, nome, cpf, senha, email):
        
        self.__id_cliente - id_cliente
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha

        self.__email = email
        

class Conta_Corrente(Conta, Operacoes_Financeiras): # Conta corrente que herda de Conta e Operacoes_Financeiras (Classe abstrata)
    def __init__(self, id_cliente, nome, cpf, senha, email, saldo_corrente, depositar, sacar, transferencia):
        super().__init__(id_cliente, nome, cpf, senha, email, depositar, sacar, transferencia)
        self.__saldo_corrente = saldo_corrente

    def getSaldoCorrente(self):
        return self.__saldo_corrente

class Conta_Poupanca(Conta, Operacoes_Financeiras): # Conta corrente que herda de Conta e Operacoes_Financeiras (Classe abstrata)
    def __init__(self, id_cliente, nome, cpf, senha, email, saldo_poupanca, depositar, sacar, transferencia):
        super().__init__(id_cliente, nome, cpf, senha, email, depositar, sacar, transferencia)
        self.__saldo_poupanca = saldo_poupanca

    def getSaldoPoupanca(self):
        return self.__saldo_poupanca

class Extrato: # classe que vai gerenciar o extrato
    def __init__(self):
        pass