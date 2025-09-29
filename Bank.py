def menu():
    pass

def deposito():
    pass

def saque():
    pass

def extrato():
    pass

print("Seja bem vindo ao Banco!")

print("[1] Depósitos\n" \
"[2] Saques\n" \
"[3] Extratos\n" \
"[4] Sair")

op = input("Informe a opção desejada!")


while True:
    match op:
        case 1:
            deposito()
        case 2:
            saque()
        case 3:
            extrato()
        case 4:
            break
        case _:
            print("ERRO! Informe uma opção válida!")