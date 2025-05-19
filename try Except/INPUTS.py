def input_int(mensagem):
    while True:
        try:
            escolha = int(input(mensagem))
            return escolha
            
        except ValueError:
            print("Digite somente os números por ex:4")

def input_float(mensagem):
    while True:
        try:
            escolha = float(input(mensagem))
            return escolha
            
        except ValueError:
            print("Digite somente os números por ex:4")
        
def input_str(mensagem):
    while True:
        escolha = str(input(mensagem))
        if not escolha.isalpha():
            print("Digite apenas letras")
        else:
            return escolha
        
        