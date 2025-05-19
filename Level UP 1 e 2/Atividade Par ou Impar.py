import random

n_aleatorio = random.randint(1,10)
while True:
    print("Menu")
    
    print("Escolha Impar ou Par")
    print("[1] - Impar")
    print("[2] - Par")
    print("[3] - Parar")
    
    jogo = int(input("Escolha uma opção: "))

    if jogo == 1:
        num = print("Você escolheu impar")
        print("Seu oponente escolheu par")
        num1 = int(input("Escolha um número para começar o jogo (1 a 10): "))
        soma = num1 + n_aleatorio
        if soma % 2 == 0:
            print("Seu jogo deu Par")
            
            print("Seu oponente escolheu:", n_aleatorio)
            print("O resultado foi", soma)
            print("Você perdeu")
        else:
            print("Seu jogo deu Impar")
            
            print("Seu oponente escolheu:", n_aleatorio)
            print("O resultado foi:", soma)
            print("Voce ganhou", soma)
    elif jogo == 2:
            num = print("Você escolheu Par")
            print("Seu oponente escolheu impar")
            num1 = int(input("Escolha um numero para começar o jogo(1 a 10): "))
            soma = num1 + n_aleatorio
            if soma % 2 == 0:
                print("Seu jogo deu Par")
                
                print("Seu oponente escolheu", n_aleatorio)
                print("O resultado é", soma)
                print("Voce ganhou")
            else:
                print("Seu jogo deu impar")
                print("voce perdeu", soma)
    elif jogo == 3:
        print("Até mais")
        break 
            
