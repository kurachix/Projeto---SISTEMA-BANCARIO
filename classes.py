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
    
    #Metodos de gerenciamento de clientes
    def adicionar_cliente(self, cliente):
        if cliente not in self.__clientes:
            self.__clientes.append(cliente)
    

class Cliente: # Classe pasa gerenciar as ações do cliente
    def __init__(self, nome : str, cpf : str, senha : str):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__contas = [] #Associação - cliente pode ter varias contas

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
    
    def adicionar_conta(self,conta):
        if conta not in self.__contas:
            self.__contas.append(conta)


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
    

class Conta(Operacoes_Financeiras, ABC): # Classe abstrata para gerenciar a conta corrente e poupança
    def __init__(self, id_conta : str, cliente: Cliente):
        self.__id_conta = id_conta
        self.__cliente = cliente
        self._saldo = 0.0
        self.__extrato = Extrato()

    def getIdConta(self):
        return self.__id_conta
    
    def getCliente(self):
        return self.__cliente
    
    def getSaldo(self):
        return self._saldo
    
    def getExtrato(self):
        return self.__extrato 
    
    def __str__(self):
        return f"Conta {self.__id_conta} - Titular: {self.__cliente.getNome()}"
    
class Conta_Corrente(Conta): # Conta corrente que herda de Conta.
    def __init__(self, id_conta: str, cliente: Cliente):
        super().__init__(id_conta, cliente)

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor Inválido!")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para essa transação")
        self._saldo -= valor
        self.getExtrato().adicionar_transacao("Saque -", -valor)

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            self.getExtrato().adicionar_transacao("Depósito -", valor )
        else:
            #Força um erro, porque nao faz sentido depositar valor negativo ou zero
            raise ValueError("Valor de depósito inválido.") 
        
    def transferencia(self, destino, valor : float):
        if valor <= 0 or valor > self._saldo:
            raise ValueError("Não foi possivel concluir essa transação pois ela é Inválida!")
        self.sacar(valor)
        destino.depositar(valor)
        self.getExtrato().adicionar_transacao(
            f"Transferencia para {destino.getCliente().getNome()}", - valor)

class Conta_Poupanca(Conta, Operacoes_Financeiras): # Conta corrente que herda de Conta e Operacoes_Financeiras (Classe abstrata)
    def __init__(self, id_cliente, nome, cpf, senha, email, saldo_poupanca, depositar, sacar, transferencia):
        super().__init__(id_cliente, nome, cpf, senha, email, depositar, sacar, transferencia)
        self.__saldo_poupanca = saldo_poupanca
    
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

    def transferencia(self, destino, valor):
        pass

    def getSaldoPoupanca(self):
        return self.__saldo_poupanca

class Extrato: # classe que vai gerenciar o extrato
    def __init__(self):
        self.__transacoes = []

    def adicionar_transacao(self, descricao, valor):
        self.__transacoes.append((descricao, valor))

    def get_transacoes(self):
        return self.__transacoes


