# Arquivo para armazenar as classes do projeto
from datetime import datetime
from abc import ABC, abstractmethod

# Classe que representa o banco 
class Banco:
    
    def __init__(self, nome: str, localizacao : str, agencia : str):
        
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
    
    def getContas(self):
        return self.__contas
    
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
    def transferir(self, destino, valor:float):
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
            raise ValueError("Valor Inválido!") #com o raise lançamos um erro, do tipo ValueError( Erro para valores invalidos)
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
        
    def transferir(self, conta_destino, valor):
        if valor <= 0:
            raise ValueError("Valor inválido para transferência.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para transferência.")

        self._saldo -= valor
        conta_destino.depositar(valor)
        self.getExtrato().adicionar_transacao(f"Transferência enviada -", -valor)
        conta_destino.getExtrato().adicionar_transacao(f"Transferência recebida -", valor)



class Conta_Poupanca(Conta): # Conta corrente que herda de Conta.
    SaldoMinimoSaque = 100.0 #Saldo minimo para fazer saque, pedido pelo nosso professor carlin

    def __init__(self, id_conta: str, cliente: Cliente):
        super().__init__(id_conta, cliente)
    
    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("Transação Inválida!")
        if (self._saldo - valor) < Conta_Poupanca.SaldoMinimoSaque:
            raise ValueError("Infelizmente, o seu saldo nao atinge o valor minimo de saque de R$100,00.")
        self._saldo -= valor
        self.getExtrato().adicionar_transacao("Saque -", - valor)

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            self.getExtrato().adicionar_transacao("Depósito -", valor)
        else:
            #Força um erro pois é maluquice depositar um valor menor que zero, né carlinho!
            raise ValueError("Valor de deposito invalido!")

    def transferir(self, conta_destino, valor):
        if valor <= 0:
            raise ValueError("Valor inválido para transferência.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para transferência.")

        self.__saldo -= valor
        conta_destino.depositar(valor)
        self.getExtrato().adicionar_transacao(f"Transferência enviada -", -valor)
        conta_destino.getExtrato().adicionar_transacao(f"Transferência recebida -", valor)




class Extrato: # classe que vai gerenciar o extrato
    def __init__(self):
        self.__transacoes = []
        
    def adicionar_transacao(self, descricao : str, valor : float):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__transacoes.append((data ,descricao, valor))

    def get_transacoes(self):
        return self.__transacoes

    def mostrar_extrato(self):
        print("Extrato")
        for data, descricao, valor in self.__transacoes:
            print(f"{data} - {descricao}: R${valor:.2f}")
