
## Desafio banco V1

LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIA = 3

extrato = 0
vezes_sacadas = 0

while(True):
    print('''
    [d] depositar
    [s] sacar
    [e] extrato
    ''')
    opcao = input("Informe sua opção: ")

    if(opcao == "d"):
        depositar_quantia = float(input("Quanto você quer depositar?"))
        extrato += depositar_quantia

    elif(opcao == "s"):
        sacar_quantia = float(input("Quanto você quer sacar?"))
        if(extrato <= 0 or sacar_quantia > 500.00 or vezes_sacadas >= 3):
            print("Falha na operação!")
        else:
            extrato -= sacar_quantia
            vezes_sacadas += 1

    elif(opcao == "e"):
        print(f"seu extrato é R${extrato}")

    else:
        break