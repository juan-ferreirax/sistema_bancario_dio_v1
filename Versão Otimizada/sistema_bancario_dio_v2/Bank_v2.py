from modulos_v2 import (
    blue, reset,
    menu, erro, concluir,
    depositar, sacar, exibir_extrato, criar_conta, listar_contas, criar_usuario
)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        menu()
        op = int(input(f"{blue}Informe a opção desejada: {reset}"))
        match op:
            case 1:
                valor = float(input("Informe o valor do deposito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
            case 2:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(
                    saldo = saldo,
                    valor = valor,
                    extrato = extrato,
                    limite = limite,
                    numero_saques = numero_saques,
                    limite_saques = LIMITE_SAQUES,
                )
            case 3:
                exibir_extrato(saldo, extrato = extrato)
            case 4:
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta: #Verificação para evitar adicionar contas vazias
                    contas.append(conta)
            case 5:
                listar_contas(contas)
            case 6:
                criar_usuario(usuarios)
            case 7:
                concluir("APLICAÇÃO FINALIZADA COM SUCESSO!")
                break
            case _:
                erro("ERRO! INFORME UMA OPÇÃO VÁLIDA!")
main()