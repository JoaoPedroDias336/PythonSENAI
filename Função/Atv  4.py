#calculadora imc

def calcule_imc (peso , altura):
    imc = peso / (altura * altura)
    return imc

    
def classificacao(imc):
    if imc <= 18.5:
        print("magreza")
    elif imc >= 18.5 and imc <=24.9:
        print("normal")
    elif imc >=25 and imc <=29.9:
        print("sobrepeso")
    elif imc >=30 and imc <=34.9:
        print("obesidade grau 1")
    elif imc >=35 and imc <=39.9:
        print("obesidade grau 2")
    elif imc >=40:
        print("obesidade grau 3")

peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = calcule_imc(peso, altura)

print("O seu IMC é", calcule_imc(peso , altura))
classificacao(imc)

