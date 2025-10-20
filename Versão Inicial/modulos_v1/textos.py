from modulos.cor import yellow, reset

def linha():
    print(yellow + "-" * 30 + reset)

def mensagem(msg):
    print(yellow + "-" * 30)
    print(f"{msg}".center(30))
    print("-" * 30 + reset)

def menu():
    print("[1] Depósitos\n" \
    "[2] Saques\n" \
    "[3] Extratos\n" \
    "[4] Sair")
    linha()