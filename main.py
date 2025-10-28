# ---------------------------------------------------------------------------------------------------------------- #
# Arquivo principal do projeto

from classes import *      # importa todas as classes
from functions import *    # importa as funções auxiliares e utilitárias

# Instancia o banco
banco = Banco("Banco SPX", "Jundiaí-SP", "Agência - 0001")

# Tela de abertura
tela_inicio()

# ---------------------------------------------------------------------------------------------------------------- #
# LOOP GERAL DO SISTEMA
# (permite logar e deslogar várias vezes sem encerrar o programa)
while True:
    cliente_logado = None  # reseta o cliente logado a cada novo ciclo

    # ---------------------- LOOP DE LOGIN / CADASTRO ---------------------- #
    while not cliente_logado:
        menu_login()

        try:
            escolha_login = int(input("\nEscolha uma opção!!!\n--> "))
        except ValueError:
            limpar_terminal()
            print("Escolha Inválida!!!\nPor favor, adicione apenas números.")
            espera_terminal()
            continue

        match escolha_login:

            case 1:  # Realizar Login
                cliente_logado = login_cliente(banco)
                if not cliente_logado:
                    limpar_terminal()
                    print("Falha no login! Verifique seus dados e tente novamente.")
                    espera_terminal()

            case 2:  # Cadastrar usuário
                cadastrar_cliente(banco)

            case 3:  # Encerrar o software
                limpar_terminal()
                print("Encerrando o software... Até logo!")
                espera_terminal()
                exit()

            case _:  # Opção inválida
                limpar_terminal()
                print("Opção inválida. Tente novamente!")
                espera_terminal()

    # ---------------------- MENU PRINCIPAL DO CLIENTE ---------------------- #
    while cliente_logado:
        menu_principal()

        try:
            escolha_usuario = int(input("\nEscolha uma opção!\n-> "))
        except ValueError:
            limpar_terminal()
            print("Escolha Inválida!!!\nPor favor, adicione apenas números.")
            espera_terminal()
            continue

        match escolha_usuario:

            # ---------------------- SAQUE ---------------------- #
            case 1:
                limpar_terminal()
                print("=== SAQUE ===")
                try:
                    valor = float(input("Informe o valor a sacar: R$"))
                    #cliente_logado representa o usuário logado no sistema.
                    conta = cliente_logado.conta_ativa
                    conta.sacar(valor)
                    limpar_terminal()
                    print(f"Saque de R${valor:.2f} realizado com sucesso!")
                except ValueError as e :
                    limpar_terminal()
                    print(f"Erro: {e}")
                espera_terminal()

            # ---------------------- DEPÓSITO ---------------------- #
            case 2:
                limpar_terminal()
                print("=== DEPÓSITO ===")
                try:
                    valor = float(input("Informe o valor a depositar: R$"))
                    conta = cliente_logado.conta_ativa
                    conta.depositar(valor)
                    limpar_terminal()
                    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
                except ValueError as e:
                    limpar_terminal()
                    print(f"Erro: {e}")
                espera_terminal()

            # ---------------------- CONSULTAR SALDO ---------------------- #
            case 3:
                limpar_terminal()
                conta = cliente_logado.getContas()[0]
                print(f"Saldo atual: R${conta.getSaldo():.2f}")
                espera_terminal()

            # ---------------------- CONSULTAR EXTRATO ---------------------- #
            case 4:
                limpar_terminal()
                conta = cliente_logado.getContas()[0]
                conta.getExtrato().mostrar_extrato()
                espera_terminal()

            # ---------------------- ALTERAR INFORMAÇÕES ---------------------- #
            case 5:
                limpar_terminal()
                print("=== ALTERAR INFORMAÇÕES ===")
                print("1 - Alterar nome")
                print("2 - Alterar CPF")
                print("3 - Alterar senha")
                print("4 - Voltar")
                try:
                    escolha = int(input("\nEscolha uma opção: "))
                    match escolha:
                        case 1:
                            novo_nome = input("Novo nome: ")
                            cliente_logado.setNome(novo_nome)
                            print("Nome alterado com sucesso!")
                        case 2:
                            novo_cpf = input("Novo CPF: ")
                            cliente_logado.setCpf(novo_cpf)
                            print("CPF alterado com sucesso!")
                        case 3:
                            nova_senha = input("Nova senha: ")
                            cliente_logado.setSenha(nova_senha)
                            print("Senha alterada com sucesso!")
                        case 4:
                            pass
                        case _:
                            print("Opção inválida.")
                except ValueError:
                    print("Digite apenas números.")
                espera_terminal()

            # ---------------------- SAIR DA CONTA ---------------------- #
            case 6:
                limpar_terminal()
                print("Saindo da conta...")
                espera_terminal()
                cliente_logado = None  # volta ao menu de login
                break

            # ---------------------- ENCERRAR SISTEMA ---------------------- #
            case 7:
                limpar_terminal()
                print("Encerrando o software... Até logo!")
                espera_terminal()
                exit()

            # ---------------------- TRANSFERÊNCIA ---------------------- #
            case 8:
                limpar_terminal()
                print("=== TRANSFERÊNCIA ===")
                cpf_destino = input("Informe o CPF do destinatário: ")

                try:
                    valor = float(input("Informe o valor a transferir: R$"))
                    conta_origem = cliente_logado._Cliente__contas[0]

                    # Busca cliente destino
                    cliente_destino = None
                    for c in banco.get_clientes():
                        if c.getCpf() == cpf_destino:
                            cliente_destino = c
                            break

                    if cliente_destino is None:
                        limpar_terminal()
                        print("Cliente destinatário não encontrado.")
                        espera_terminal()
                        continue

                    conta_destino = cliente_destino._Cliente__contas[0]
                    conta_origem.transferir(conta_destino, valor)

                    limpar_terminal()
                    print(f"Transferência de R${valor:.2f} realizada com sucesso para {cliente_destino.getNome()}!")

                except ValueError as e:
                    limpar_terminal()
                    print(f"Erro: {e}")
                espera_terminal()

            # ---------------------- OPÇÃO INVÁLIDA ---------------------- #
            case _:
                limpar_terminal()
                print("Opção inválida. Tente novamente!")
                espera_terminal()
