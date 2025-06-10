peso = float(input("Digite o peso"))
distancia = float(input("Digite a distancia"))
taxa = 20
def calcula_frete(peso, distancia, taxa):
    peso1 = peso * 0.5
    distancia1 = distancia * 0.1
    valor = peso1 + distancia1 + taxa
    
    print("o valor do frete é: ", valor)
    
calcula_frete(peso, distancia, taxa)