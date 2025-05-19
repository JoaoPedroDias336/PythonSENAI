def menu_calculadora():
    print("")
    print("Escolha uma opção:")
    print("1 - soma")
    print("2 - subtração")
    print("3 - divisao")
    print("4 - multiplicação")
    
menu_calculadora()


resposta = int(input('escolha uma operação'))

if resposta == 1:
    num1 = float(input("Digite um número:"))
    num2 = float(input("Digite outro número novamente"))
    print("o resultado da soma é:", num1 + num2)

elif resposta == 2:
    num1 = float(input("Digite um número:"))
    num2 = float(input("Digite outro número novamente"))
    print("o resultado da soma é:", num1 - num2)
    
elif resposta == 3:
    num1 = float(input("Digite um número:"))
    num2 = float(input("Digite outro número novamente"))
    print("o resultado da soma é:", num1 / num2)
    
elif resposta == 4:
    num1 = float(input("Digite um número:"))
    num2 = float(input("Digite outro número novamente"))
    print("o resultado da soma é:", num1 * num2)
    


