from datetime import datetime

nome = input("digite seu nome")

def hora2():
    hora = datetime.now().hour
    return hora

def saudacao():
    if hora2() >= 0 and hora2() <= 5:
        print("Tenha um Boa madrugada", nome)
    elif hora2() >= 5 and hora2() <= 12:
        print("Tenha um Bom dia", nome)
    elif hora2() >= 12 and hora2() <= 19:
        print("Tenha uma Boa Tarde", nome)
    elif hora2() >= 19 and hora2() <= 23:
        print("Tenha uma Boa Noite", nome)
        
    
saudacao()