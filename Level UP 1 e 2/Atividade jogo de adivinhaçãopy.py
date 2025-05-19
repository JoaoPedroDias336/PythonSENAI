import random

jp = random.randint(0,100)
def menu():
    print("Vamos jogar")
    print("Adivinhe um numero (0 a 100)")
    print("Deseja continuar")
    print("[1] - continuar")
    print("[2] - sair")

menu()
nume = int(input("digite a opção:"))

if nume == 1:
    while True:
       
        num = int(input("coloca o seu numero"))
        if num == jp:
            print("seu numero ta certo", "ele é", jp)
            menu()
            jp = random.randint(0,100)
            nume = int(input("coloque a opção"))
            if nume == 2:
                print("até mais")
                break
            
        elif jp > num:
            print("seu numero é maior que", num)
        
        elif jp < num:
            print("Seu numero é menor que", num)
            
elif nume == 2:
    print("Até mais")