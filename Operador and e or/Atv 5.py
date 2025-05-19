print("Vamos calcular!")
num = int(input("Digite um número: "))
num2 = int(input("Digite outro número novamente: "))

operacao = input("Digite a operação que você deseja (+,-,*,/): ")



soma = num + num2

subtracao = num - num2

multiplicacao = num * num2

divisao = num / num2



if operacao == "+":
    print("Seu resultado é:", soma)

elif operacao == "-":
    print("Seu resultado é:", subtracao)
    

elif operacao == "*":
    print("Seu resultado é:", multiplicacao)
    

elif operacao == "/":
    print("Seu resultado é:", divisao)
    

else:
    print("Operação desconhecida")