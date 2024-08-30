def depositar(saldo: float, historico_extrato: list)-> float:
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

def sacar(saldo: float, historico_extrato: list,limite_saques: int):
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
    
def extrato(historico_extrato: list) -> None:
    print('____________________________________________________________')
    if historico_extrato:
        for dicionario in historico_extrato:
            print(f'Operação: {dicionario['Operação']},  Valor: R${dicionario['Valor']:.2f},    Saldo: R${dicionario['Saldo']:.2f}')
    else:
        print('Sem operações realizadas')
    print('____________________________________________________________')
            

menu = """_______________
Menu
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
_______________
=> """

saldo = 0
limite_saques = 3
historico_extrato = []

while True:
    print(menu, end=" ")
    opcao = input('Digite uma das operações do menu:')
    match opcao:
        case 'd':
            saldo = depositar(saldo,historico_extrato)
        case 's':
            saldo,limite_saques = sacar(saldo,historico_extrato,limite_saques)
        case 'e':
            extrato(historico_extrato)
        case 'q':
            print('Adeus')
            break
        case _:
            print('Digite uma tecla válida')
       
        