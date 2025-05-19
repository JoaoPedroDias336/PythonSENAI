nota = int(input("Insire sua nota: "))
nota2 = int(input("Insire uma outra nota novamente: "))

soma = nota + nota2
divisao = soma / 2
if nota > 0 and nota <= 100 and nota2 >= 0 and nota2 <= 100:

    if divisao >= 70:
        print("Aprovado")
    elif divisao >= 50 and divisao < 70:
        print("Recuperação")
    elif divisao < 50:
        print("Recuperação")
    
    
    print("Sua nota foi:", divisao)
else:
    print("Digite um número de 0 á 100")
        
    