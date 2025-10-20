# Operações realizadas pela aplicação bancária
from .cores import red, yellow, reset
from .exibicao import linha, mensagem, concluir, erro

def depositar(saldo, valor, extrato, /): #tudo antes da / será obrigatoriamente parâmetros posicionais
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: \tR$ {valor:.2f}\n"
        concluir("DEPOSITO REALIZADO COM SUCESSO!")
    else:
        erro("ERRO! O valor informado é inválido!")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # todos os argumentos depois do * serão obrigatoriamente nomeados(chaveados)
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        erro("ERRO! Você não tem saldo suficiente!")
    elif excedeu_limite:
        erro("ERRO! O valor de saque informado excede o limite disponível!")
    elif excedeu_saques:
        erro("ERRO! Número máximo de saques excedido!")
    elif valor > 0:
        saldo -= valor
        extrato +=  f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        concluir("SAQUE REALIZADO COM SUCESSO!")
    else:
        erro("ERRO! O valor informado é inválido!")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    mensagem("EXTRATO")
    print(f"{yellow}NÃO FORAM REALIZADAS MOVIMENTAÇÕES!{reset}" if not extrato else extrato)
    print(f"Saldo: \t\tR$ {saldo:.2f}")
    linha()

def criar_usuario(usuarios):
    cpf = int(input("Informe o CPF(somente números): "))
    usuario = filtrar_usuário(cpf, usuarios)

    if usuario:
        print(f"{yellow}JÁ EXISTE UM USUÁRIO COM ESSE CPF!{reset}")
        return
    
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereço": endereco})
    concluir("USUÁRIO CADASTRADO COM SUCESSO!")

def filtrar_usuário(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF(somente números): "))
    usuario = filtrar_usuário(cpf, usuarios)

    if usuario:
        concluir("CONTA CRIADA COM SUCESSO!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    erro("Usuário não encontrado! Interrompendo fluxo de criação de conta...")

def listar_contas(contas):
    if not contas:
        erro("ERRO! AINDA NÃO HÁ CONTAS CADASTRADAS!")
        return

    for conta in contas:
        linha()
        print(f"Agência:	{conta['agencia']}")
        print(f"C/C:		{conta['numero_conta']}")
        print(f"Titular:	{conta['usuario']['nome']}")
    linha()