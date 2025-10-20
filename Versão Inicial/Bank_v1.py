from modulos_v1.textos import menu, mensagem
from modulos_v1.cor import green, red, blue, reset
from modulos_v1.operacoes import deposito, saque, extrato

mensagem("Welcome to the Bank")
while True:
    menu()
    op = int(input(f"{blue}Informe a opção desejada: {reset}"))
    match op:
        case 1:
            deposito()
        case 2:
            saque()
        case 3:
            extrato()
        case 4:
            print(f"{green}APLICAÇÃO FINALIZADA COM SUCESSO!{reset}")
            break
        case _:
            print(f"{red}ERRO! Informe uma opção válida!{reset}")