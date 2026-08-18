import calculadora

def menu():
    while True:
        print("1. Somar")        

        opcao = int(input("Escolha uma opção: "))        

        if opcao == 1:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print (f'{a} + {b} = {calculadora.somar(a, b)}')