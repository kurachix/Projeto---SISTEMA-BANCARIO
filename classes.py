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


class Cliente: # classe que vai servir como representação de um cliente do banco.

    # Atributos privados
    def __init__(self, nome, cpf, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha

    # método para verificar se a senha esta correta
    def verificar_senha(self, senha):
        return self.__senha == senha

    # Getters
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf
    
class Conta:
    pass

class Extrato:
    pass

class ContaCorrente(Conta):
    pass

class ContaPoupança(Conta):
    pass   
        


    

