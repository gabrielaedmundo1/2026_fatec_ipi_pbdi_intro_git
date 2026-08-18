import calculadora

def menu():
    while True:
        print("1. Somar")        
        print("2. Subtrair")  
        print("3. Multiplicar")  

        opcao = int(input("\nEscolha uma opção: "))        

        if opcao == 1:
            a = float(input("\nDigite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print (f'\n{a} + {b} = {calculadora.somar(a, b)}')

        if opcao == 2:
            a = float(input("\nDigite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print (f'\n{a} - {b} = {calculadora.subtrair(a, b)}')

        if opcao == 3:
            a = float(input("\nDigite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print (f'\n{a} * {b} = {calculadora.multiplicar(a, b)}')