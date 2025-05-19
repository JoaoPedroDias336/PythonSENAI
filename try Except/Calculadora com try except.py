def menu_calculadora():
    print("Menu")
    print("")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - todas")
    while True:
        try:
            escolha = int(input("Escolha qualquer um dos números acima:"))
            break
        
        except ValueError:
            print("Digite somente os números por ex:4")
            
            
    while True:
        try:
            num1 = float(input("Digite um número!:"))
            break
        
        except ValueError:
            print("Digite somente os números por ex:4")
            
    while True:
        try:
            num2 = float(input("Digite outro número novamente!:"))
            break
        except ValueError:
            print("Digite somente os números por ex:4")
         
         

    if escolha == 1:
        print("O resultado da adição ficou" , soma(num1,num2))
    elif escolha == 2:
        print("O resultado da subtração ficou" , subtração(num1,num2))
    elif escolha == 3:
        print("O resultado da multiplicação ficou" , multiplicação(num1,num2))
    elif escolha == 4:
        print("O resultado da divisão ficou" , divisão(num1,num2))
    elif escolha == 5:
        resposta(num1,num2)
    else:
        print("erro")
                   
def soma(num1,num2 ):
    return num1 + num2

def subtração(num1,num2):
    return num1 - num2

def multiplicação(num1,num2):
    return num1 * num2

def divisão (num1,num2):
    return num1 / num2

def resultados(num1,num2):
    print(soma (num1,num2), "Esse é o resultado da adição")
    print(subtração (num1,num2), "Esse é o resultado da subtração")
    print(multiplicação (num1,num2), "Esse é o resultado da multiplicação")
    print(divisão (num1,num2), "Esse é o resultado da divisão")


menu_calculadora()