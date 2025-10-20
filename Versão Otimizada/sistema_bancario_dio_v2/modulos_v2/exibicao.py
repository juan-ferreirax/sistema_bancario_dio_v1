# Exibição do menu e linhas para organização das informações
from .cores import yellow, reset, red, green

def linha():
    print(yellow + "-" * 30 + reset)

def erro(msg):
    print(f"{red}{msg}{reset}")

def concluir(msg):
    print(f"{green}{msg}{reset}")

def mensagem(msg):
    print(yellow + "-" * 30)
    print(f"{msg}".center(30))
    print("-" * 30 + reset)

def menu():
    mensagem("Welcome to the Bank")
    print("[1] Depósitar\n" \
    "[2] Sacar\n" \
    "[3] Extrato\n" \
    "[4] Nova conta\n" \
    "[5] Listar conta\n" \
    "[6] Novo usuário\n" \
    "[7] Sair")
    linha()