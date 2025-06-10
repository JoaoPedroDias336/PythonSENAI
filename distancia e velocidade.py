def verificar(distancia, velocidade):
    tempo = distancia/velocidade
    print("O tempo sera de", tempo, "horas")



print("calculando o tempo levara ao percurso")
distancia = int(input("Coloque a distancia: "))
velocidade = int(input("Coloque a velocidade: "))

verificar(distancia, velocidade)