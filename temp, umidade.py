def verificar(temperatura, umidade, escolha):
    if escolha == "inverno":
        if temperatura >= 20 and temperatura <= 22:
            if umidade >= 40 and umidade <= 55:
                print("A qualidade do ar esta adequada para o inverno! ")
            else:
                print("A qualidade do ar não esta boa! ")
        elif escolha == "verao":
            if temperatura >= 23 and temperatura <=26:
                if umidade >= 56 and umidade <= 65:
                    print("a qualidade do ar nao esta boa para o verao! ")
                else:
                    print("A qualidade do ar nao esta boa ")
escolha = str(input("coloque aqui a estação inverno ou verão: "))
temperatura = int(input("escreva a temperatura: "))
umidade = int(input("agora escreva a umidade: "))
verificar(temperatura, umidade, escolha)
                