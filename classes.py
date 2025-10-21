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
