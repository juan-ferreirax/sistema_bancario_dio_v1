from modulos.cor import green, red, yellow, blue, reset
from modulos.textos import linha, mensagem

saldo = 0
quant_saques = 3
extrato_bancario = []

def deposito():
    global saldo
    deposito = {}
    while True:
        valor = float(input(f"{yellow}Informe um valor para depósito: {reset}"))
        if valor > 0:
            break
        else:
            print(f"{red}ERRO! Informe um valor válido!")
            pass
    deposito["Deposito"] = valor
    extrato_bancario.append(deposito.copy())
    saldo += valor
    print(f"{green}DEPOSITO REALIZADO COM SUCESSO!{reset}")
    print(f"Seu saldo atual é de R$ {saldo:.2f}")
    linha()

def saque():
    global quant_saques, saldo
    saque = {}
    if quant_saques == 0:
        print(f"{red}ERRO! O limite de saques diários já foi excedido!{reset}")
    else:
        valor = float(input(f"{yellow}Informe o valor a ser sacado: {reset}"))
        if valor >= 0.05 and valor <= 500:
            if valor <= saldo:
                saque["Saque"] = valor
                extrato_bancario.append(saque.copy())
                saldo -= valor
                print(f"{green}SAQUE REALIZADO COM SUCESSO!{reset}")
                print(f"Seu saldo atual é de R$ {saldo:.2f}")
                linha()
                quant_saques -= 1
            else:
                print(f"{red}ERRO! Você não possui saldo suficiente!{reset}")
        else:
            print(f"{red}ERRO! Escolha um valor entre R$ 0,05 e R$ 500,00{reset}")

def extrato():
    mensagem("Extrato Bancário")
    for transacoes in extrato_bancario:
        for transacao, valor in transacoes.items():
            print(f"{transacao:<18} R$ {valor:.2f}")
    linha()        
    print(f"Saldo".ljust(19) + "R$ " + f"{saldo:.2f}")
    linha()