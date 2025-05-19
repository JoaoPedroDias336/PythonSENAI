nota1 = int(input("Digite sua primeira nota"))
nota2 = int(input("Digite sua segunda nota"))


soma = nota1 + nota2
media = soma / 2

variavel = ""

if media >= 70:
    variavel = "Aprovado"
elif media < 70:
    variavel = "Reprovado"
print(media, "Você foi", variavel)