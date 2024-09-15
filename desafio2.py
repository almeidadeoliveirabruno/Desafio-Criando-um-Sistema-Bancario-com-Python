import pprint 
def depositar(saldo: float, historico_extrato: list, /)-> float:
    while True:
        deposito = input('Digite um valor para o depósito: ')
        if deposito == 'q':
                print('Operação Cancelada')
                return saldo
        try:
            deposito = float(deposito)
            if deposito > 0:
                saldo += deposito
                historico_extrato.append({'Operação':'Depósito',
                                          'Valor': deposito, 
                                          'Saldo':saldo})
                return saldo
            else:
                print('Digite um valor acima de zero ou aperte [q] para sair')
        except ValueError:
            print("Entrada inválida, Digite um número ou aperte [q] para sair")

def criar_usuario(usuarios: list):
    usuario = {}
    usuario['Nome'] = input('Nome: ')
    usuario['Data_Nascimento'] = input('Data de Nascimento: ')
    usuario['cpf'] = verifica_cpf()
    usuario['Logradouro'] = input('Logradouro: ')
    usuario['Nro'] = input('Nro: ')
    usuario['Bairro'] = input('Bairro: ')
    usuario['Cidade'] = input('Cidade: ')
    usuario['Estado'] = input('Estado: ')
    cadastro = verifica_usuario_cadastrado(usuario['cpf'],usuarios)
    if cadastro:
        return print('Não foi possível cadastrar: Usuário já cadastrado ')
    usuarios.append(usuario)
    print('Usuário criado')
    
def verifica_cpf():
 while True:
    cpf = input('Digite o cpf(Apenas os números): ')
    if cpf.isnumeric():
        return cpf
    print('Cpf inválido! Digite apenas números')

def verifica_usuario_cadastrado(cpf: str,lista_usuarios: list):
    usuario = list(filter(lambda usuario: usuario['cpf'] == cpf,lista_usuarios))
    return usuario

def sacar(*,saldo: float, historico_extrato: list,limite_saques: int):
    while True:
        if limite_saques == 0:
            print('Você não pode sacar mais hoje')
            return saldo,limite_saques

        saque = input('Digite um valor para Saque: ')
        if saque =='q':
                print('Operação Cancelada')
                return saldo,limite_saques
        try:
            saque = float(saque)
        except ValueError:
            print('Digite um número ou aperte [q] para sair')
            continue

        if saque > saldo:
            print('Saldo Insuficiente. Digite um novo valor ou aperte [q] para sair')
            continue
        elif saque > 500:
            print('O valor de saque ultrapassa o limite de R$ 500,00.Digite um novo valor ou aperte [q] para sair  ')
            continue
        elif saque <= 0:
            print('Digite um valor válido maior que 0')
            continue

        saldo -= saque
        historico_extrato.append({'Operação': 'Saque',
                                  'Valor': saque,
                                  'Saldo':saldo})
        limite_saques -= 1
        return saldo,limite_saques
    
def extrato(historico_extrato: list,*, saldo: float) -> None:
    print('____________________________________________________________')
    print(f'Saldo: R${saldo}')
    if historico_extrato:
        for dicionario in historico_extrato:
            print(f'Operação: {dicionario['Operação']},  Valor: R${dicionario['Valor']:.2f},    Saldo: R${dicionario['Saldo']:.2f}')
    else:
        print('Sem operações realizadas')
    print('____________________________________________________________')
            
def criar_conta(usuarios:list, conta:list):
    nova_conta = {'Agencia': '0001'}
    nova_conta['Número_conta'] = len(conta) + 1
    cpf = input('Digite o cpf do usuário(Números apenas): ')
    usuario = verifica_usuario_cadastrado(cpf,usuarios)
    if not usuario:
        print('Usuário não encontrado')
        return
    nova_conta['Usuário'] = usuario
    conta.append(nova_conta)
    print('Conta criada com Sucesso')

def listar_usuarios(usuarios:list):
    if not usuarios:
        print('Não existem usuarios registradas')
        return
    for usuario in usuarios:
        pprint.pprint(usuario)
        print()

def listar_contas(conta:list):
    if not conta:
        print('Não existem contas registradas')
        return
    for contas in conta:
        pprint.pprint(contas)
        print()

menu = """_______________
Menu
[u] Criar Usuário
[c] Criar Conta
[lc] Listar Contas
[lu] Listar Usuários
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
_______________
=> """

saldo = 0
limite_saques = 3
historico_extrato = []
usuario = []
conta = []

while True:
    print(menu, end=" ")
    opcao = input('Digite uma das operações do menu:')
    match opcao:
        case 'u':
            criar_usuario(usuario)
        case 'lc':
            listar_contas(conta)
        case 'lu':
            listar_usuarios(usuario)
        case 'c':
            criar_conta(usuario,conta)
        case 'd':
            saldo = depositar(saldo, historico_extrato)
        case 's':
            saldo,limite_saques = sacar(saldo=saldo, historico_extrato=historico_extrato, limite_saques=limite_saques)
        case 'e':
            extrato(historico_extrato,saldo = saldo)
        case 'q':
            print('Adeus')
            break
        case _:
            print('Digite uma tecla válida')
       
        